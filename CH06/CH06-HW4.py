score={'하준':90,'서윤':86,'지아':80}
print(score)

score['수지']=95
print(score)

del score['지아']
print(score)

score2={'기창':90,'남철':60,'기성':75}
score.update(score2)
print(score)
