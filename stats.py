import pymysql.cursors
from pychord import Chord
from collections import Counter
from itertools import chain, combinations

#note: added ('m6', (0, 3, 7, 9)) to QUALITY_DICT in pychord\constants\qualities.py

def fix(chord):
    chord = chord.replace('maj7', 'M7').replace('maj9', 'M9').replace('(', '').replace(')', '')
    if chord.endswith('sus'):
        chord = chord.replace('sus','5')
    return chord

db = pymysql.connect(host="localhost", user="root", passwd="", db="UltimateGuitarTabs")
cur = db.cursor()

cur.execute("select chords from chords")
instances_per_song = [[fix(chord) for chord in row[0].split(',')] for row in cur.fetchall()]
chords_per_song = [set(instances) for instances in instances_per_song]
count_instances = Counter(chord for instances in instances_per_song for chord in instances)

base_chords = set()
bad_chords = {}
fold_chords = {}
seen_comps_to_chords = {}
for chord, cnt in sorted(count_instances.items(), key=lambda x:(-x[1],x[0])):
    try:
        comps = tuple(sorted(set(Chord(chord).components())))
    except:
        bad_chords[chord] = cnt
        continue
    if comps in seen_comps_to_chords:
        fold_chords[chord] = seen_comps_to_chords[comps]
    else:
        base_chords.add(chord)
        seen_comps_to_chords[comps] = chord

print(sorted(bad_chords.items(), key=lambda x: (-x[1],x[0])))
folded_per_song = [set(fold_chords[chord] if chord in fold_chords else chord for chord in chords) for chords in chords_per_song if all(chord not in bad_chords for chord in chords)]
print('base chords=%d, folded chords=%d, bad chords=%d, bad songs=%d/%d (%.1f%%)'%(len(base_chords),len(fold_chords),len(bad_chords),len(chords_per_song)-len(folded_per_song),len(chords_per_song),(len(chords_per_song)-len(folded_per_song))/len(chords_per_song)*100))

max_needed = Counter(len(a) for a in folded_per_song)
print(max_needed)

count_chords = Counter(chord for chords in folded_per_song for chord in chords)
print(count_chords)

print(sorted([(chords,cnt) for chords,cnt in Counter(tuple(sorted(chords)) for chords in folded_per_song if 3<=len(chords)<=6).items() if cnt>10], key=lambda x:(-x[1],x[1])))


#have_chords = ['G', 'C', 'D', 'Am', 'Em', 'F', 'A','Dm', 'F#m']
#have_chords = ['C', 'C7', 'A', 'Am', 'A7', 'F']
have_chords = ['A', 'Am', 'A7', 'Am7','A7sus4','Ammaj7','Amaj7','Asus4','A9','Bbdim','C', 'C7', 'C7sus4','Cmaj7','C6','Csus4','Caug','C9','Cadd9Fsus2','C#mmaj7','C#dim','Dsus2','Dsus4','Eaug','Em7','Emmaj7','F','F6sus2','Fadd9','G6','Gdim','Gsus2','G#aug']
have_chords_set = set(have_chords)
count_have = sum(chords<=have_chords_set for chords in folded_per_song)
print(have_chords, '%d/%d %.1f%%'%(count_have,len(folded_per_song),count_have/len(folded_per_song)*100))

def powerset(iterable, max_len=None):
    s = list(iterable)
    if max_len is None:
        max_len = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(1,max_len+1))

top = 16
max_len = 16
top_chords = [chord[0] for chord in sorted(count_chords.items(), key=lambda x: -x[1])][:top]
print(top_chords)
for i in range(1,max_len+1):
    subs = powerset(top_chords,i)
    best_sub = []
    best_count = 0
    for sub in subs:
        sub = sorted(sub)
        sub_set = set(sub)
        count_have = sum(chords <= sub_set for chords in folded_per_song)
        if count_have>best_count:
            best_count = count_have
            best_sub = [sub]
        elif count_have==best_count:
            best_sub.append(sub)
    if best_count>0:
        print('%d %d %.1f%%'%(i, best_count, best_count / len(folded_per_song) * 100), best_sub)