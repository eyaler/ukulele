# Uku3le
## C4 G4 A4
### Eyal Gruss and Ayelet Sapirshtein
#### For Daniel Johnston

A simpler 3-string tuning for ukulele.

Play 25% of songs - with only 2 fingers!

We optimized a ukulele tuning to allow playing chords for a maximum number of songs with a minimum number of fingers, 
and trying to give the more important chords the easier fingering. We do not allow barres nor muted strings. 
Chord importance is determined not necessarily by prevalence, but by the number of complete songs they allow playing given the other chords.
This is an optimization problem called the [densest k-subhypergraph problem](https://arxiv.org/abs/1605.04284), which we solve by brute force.

For example, the 6 most prevalent chords, counting songs are: C, D, F, G, Em, A. The 6 most prevalent chords, counting chord instances are: C, D, F, G, Am, A.
And the 6 most important chords, that is the 6 chords that allow playing the maximal number of complete songs are: C, D, F, G, Em, Am.
Which makes sense for the latter as this is just the combination of the chords of the [most popular](http://www.hooktheory.com/blog/music-theory-analysis-1300-songs-for-songwriting-part2) 
I-V-vi-IV progression for the [most popular](http://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found) C major (C-G-Am-F) and G major (G-D-Em-C) scales.
By the way, for 7 chords the three groups converge to the union of the above.

We use data of 19,358 most popular rock, pop, folk and country songs from 1960 to date, 
scraped from [Ultimate Guitar](https://www.ultimate-guitar.com). 
The scraper is based on [Ljfernando's Progressions repo](https://github.com/Ljfernando/Progressions), 
and the analysis is made possible by [pychord](https://github.com/yuma-m/pychord). 
Different from most analyses, we do not normalize the data by transposition as we want to allow users to play songs in 
their original form (Pink Floyd's "In the Flesh?" starts with an A!), we do not want to a degenerate songs with key shifts, 
and we do not want to require the user to do transpositions. 
However, in our optimization we were indifferent to the chord voicing - the octave choices for each note in the chord,
including chord inversions - change of the root note.

Considering the use of up to two fingers, our chosen tuning of C-G-A allows playing 23.3% of songs with up to 4-note chords and 42.4% of songs with up to 3-note chords, 
as compared to 0.8% and 1.4% respectively for the standard G-C-E-A tuning. 
Note that one could potentially further simplify 4-note chords to incomplete versions with 3 notes, which we did not do here. 
We do pay an additional price of needing to utilize frets number 2 to 7 to play these chords, and some other 3-note chords would even require higher frets.

Following are the chord charts for 20 popular chords requiring up to two fingers and a reach difference of up to two frets.
We hope this system may help children, perplexed beginners, people with disabilities and the dexterity-challenged to play strings.

<br/>

![ukulele-CGA](assets/ukulele-CGA.jpg)

![C](assets/00_C.svg)
![C(1)](assets/01_C(1).svg)
![Cm](assets/02_Cm.svg)
![Cm(1)](assets/03_Cm(1).svg)
![Csus4](assets/04_Csus4.svg)
![C5](assets/05_C5.svg)
![D](assets/06_D.svg)
![Dm](assets/07_Dm.svg)
![Dsus4](assets/08_Dsus4.svg)
![Dsus4(1)](assets/09_Dsus4(1).svg)
![D5](assets/10_D5.svg)
![Eb](assets/11_Eb.svg)
![Em](assets/12_Em.svg)
![F](assets/13_F.svg)
![F#m](assets/14_F%23m.svg)
![G](assets/15_G.svg)
![Gm](assets/16_Gm.svg)
![Gsus4](assets/17_Gsus4.svg)
![Gsus4(1)](assets/18_Gsus4(1).svg)
![G5](assets/19_G5.svg)
![A](assets/20_A.svg)
![Am](assets/21_Am.svg)
![Asus4](assets/22_Asus2.svg)
![A5](assets/23_A5.svg)

Here are the most important missing chords requiring 3 fingers:

![E](assets/24_E.svg)
![Bb](assets/25_Bb.svg)
![B](assets/26_B.svg)
![Bm](assets/27_Bm.svg)

Chord charts by [Chordious](https://chordious.com).

Some statistics (no transpositions, respect chord voicings, no limit on number of notes in chord):

![Chord prevalence by songs](assets/chord_prevalence_by_songs.svg)
![Chord prevalence by chord instance](assets/chord_prevalence_by_chord_instance.svg)
![Next chord prevalence by instance](assets/next_chord_prevalence_by_instance.svg)
![Number of distinct chords by songs](assets/number_of_distinct_chords_by_songs.svg)
![Chord set prevalence by songs](assets/chord_set_prevalence_by_songs.svg)
![k-length chord sets for maximum songs](assets/k-length_chord_sets_for_maximum_songs.svg)

A [Geekcon+2019](https://geekcon.org/geekcon-plus-2019) project.
