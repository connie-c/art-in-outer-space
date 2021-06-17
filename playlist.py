import os 
from pprint import pprint
from googleapiclient.discovery import build

api_key = os.environ.get('YOUTUBE_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = os.environ.get('YOUTUBE_PLAYLIST_KEY')

Videos = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails, snippet',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    video_ids = []
    for item in pl_response['items']:
        video_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="statistics, snippet",
        id=','.join(video_ids),

    )

    vid_response = vid_request.execute()
    # pprint(vid_response)

    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']

        video_id = item['id']
        yt_link = f'https://youtube.com/embed/{video_id}'
        title = item['snippet']['title']
        description = item['snippet']['description']

        Videos.append(
            {
                'video_id': video_id,
                'views': int(vid_views),
                'url': yt_link,
                'title': title,
                'description': description
            }
        )


    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

Videos.sort(key=lambda vid: vid['views'], reverse=True)

# for video in Videos[:2]:
    # print(video['url'], video['title'], video['views'], video['description'])

# print(len(Videos))

# print(Videos)