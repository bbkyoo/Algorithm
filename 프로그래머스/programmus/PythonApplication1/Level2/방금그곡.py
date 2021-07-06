def change(melody):
    if 'A#' in melody:
        melody = melody.replace('A#','a')
    if 'C#' in melody:
        melody = melody.replace('C#','c')
    if 'D#' in melody:
        melody = melody.replace('D#','d')
    if 'F#' in melody:
        melody = melody.replace('F#','f')
    if 'G#' in melody:
        melody = melody.replace('G#','g')

    return melody

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':')) # 이 부분 꼭 기억
        time = 60*(end_h-start_h) + (end_m-start_m) # 이 부분 꼭 기억해두기
        melody = change(melody)
        melody_play = (melody*time)[:time]

        if m in melody_play:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title,time)

    return answer[0]
















