"""
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
"""
# from collections import defaultdict
#
# def solution(genres, plays):
#
#     play_count_by_genre = defaultdict(int)
#     songs_in_genre = defaultdict(list)
#
#     for song_id, genre, play in zip(range(len(genres)), genres, plays):
#         print(song_id, genre, play)
#         play_count_by_genre[genre] += play
#         songs_in_genre[genre].append((-play, song_id))
#
#     genre_in_order = sorted(play_count_by_genre.keys(), key=lambda g: play_count_by_genre[g], reverse=True)
#
#     print(sorted(songs_in_genre.keys(), key= lambda h: songs_in_genre[h], reverse=True ))
#     answer = list()
#     for genre in genre_in_order:
#         print(genre)
#         answer.extend([song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])
#
#     return answer
#
# def counter():
#
#     i = 0
#     while True:
#         yield i
#         i += 1

from collections import defaultdict

def solution(genres, plays):
    answer = []
    plays_by_genres = {}
    detail_plays_by_genres = {}
    for idx, genre, play in zip(range(len(genres)), genres, plays):
        if genre in plays_by_genres.keys():
            plays_by_genres[genre] += (play * -1)
            detail_plays_by_genres[genre].append((-play, idx))
        else:
            plays_by_genres[genre] = (play * -1)
            detail_plays_by_genres[genre] = [(-play, idx)]

    plays_by_genres = sorted(plays_by_genres.keys(), key= lambda k : plays_by_genres[k])

    for gen in plays_by_genres:
        answer.extend([value for key, value in sorted(detail_plays_by_genres[gen])[:2]])

    return answer



"""
1. 전체 재생횟수가 큰 순서 대로 알고 있어 한다
2.

"""
genres =["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres,plays)

