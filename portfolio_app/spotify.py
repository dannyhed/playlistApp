from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import base64
import json

CLIENT_ID='e097fa8731da4370a95d3e9e058d6247'
CLIENT_SECRET='227b6d3a5f774270a8d06034ac276128'

accessToken = ''
refreshToken = ''

tokenData = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}

tokenHeaders = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def getToken():
    tokenResponse = requests.post('https://accounts.spotify.com/api/token', data=tokenData, headers=tokenHeaders)
    parseResponse = tokenResponse.content.decode("utf-8").split("\"")
    i = 0
    while (parseResponse[i] != "access_token"):
        i += 1
    accessToken = parseResponse[i + 2]
    return accessToken

def authorization():
    authData = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'http://localhost:8000/',
        'show_dialog': 'true',
        'scope': 'user-read-playback-state+user-modify-playback-state+user-read-currently-playing+app-remote-control+streaming+playlist-read-private+user-read-playback-position+user-library-read',
    }
    headers = {
        'Authorization': 'Bearer ' + accessToken
    }
    authString = ''
    for key in authData:
        authString += key + '=' + authData[key] + '&'
    #print(authString)
    authRequestLink = "https://accounts.spotify.com/authorize?" + authString
    return authRequestLink

def getAccessToken(code):
    #code = args.split("=")[1]
    #if (code == "access_denied"):
       # return 0
        #something
    #else:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + (base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode("utf-8"))).decode("utf-8")
    }
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/'
    }
    accessResponse = requests.post('https://accounts.spotify.com/api/token', headers=headers, params=params)
    
    accessResponseParse = accessResponse.content.decode("utf-8").split("\"")
    
    i = 0
    while (accessResponseParse[i] != "access_token"):
        i += 1
    accessToken = accessResponseParse[i + 2]
    i = 0
    while (accessResponseParse[i] != "refresh_token"):
        i += 1
    refreshToken = accessResponseParse[i + 2]
    return accessToken

def getPlaylists(code):
    headers = {
        'Authorization': 'Bearer ' + getAccessToken(code)#.encode("utf-8")
    }
    userPlaylistsResponse = requests.get('https://api.spotify.com/v1/me/playlists?limit=1&offset=0', headers=headers)
    print("PLAYLIST RESPONSE")
    print(userPlaylistsResponse)
    playlistArray = []
    #HOW TO SEARCH :(
    playlistParse = userPlaylistsResponse.content.decode("utf-8").strip("\"")
    start = playlistParse.find("items:")
    
    #for playlist in userPlaylistsResponse.content.decode("utf-8")[6]:
    #    playlistArray.append(playlist[2][0])
    return playlistArray

def getProfile():
    headers = {
        'Authorization': 'Bearer ' + accessToken
    }    
    response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    return response.content

#The response will return an access token valid for 1 hour:
#{
#  "access_token": "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11",
#  "token_type": "Bearer",
#  "expires_in": 3600
#}


