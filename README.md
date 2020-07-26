# Music-Generator
A Sine wave can be perceived as Sound Wave,
where the crest of the sine is considered as the compression of the pressure wave and trough of the former wave is the rarefaction of the later wave.
We will generate a lot of sine wave and convert them into sound, which we will export it as a .wav file.

How to give input:
                  - Enter the letter IP to the terminal(refer below table)
                  - If for a particular point 0 HZ sine wave (ie. no sound) need to be generated give '*' as letter IP
                  - each letter IP will be played for 1 sec
                  Ex:-
                  <IP:> 1e@*Q
                  This will generate a audio file 'final.wav' of 5 sec (since 5 letter IP), where for the first 1 sec it will produce the C2 note, the next 1 second it will 
                  produce A3 note then D2# note, next no sound will be generated since * is provided and in the last second it will produce F3# note.
                  
Below given the letter notes for different frequencies:
               [('IP in the terminal'),corrosponding frequency in Hz]   # Corrosponding Letter Notes
               
               [('1'),65.41]    #   c2
               [('2'),73.42]    #   d2
               [('3'),82.41]    #   e2
               [('4'),87.31]    #   f2
               [('5'),98]       #   g2
               [('6'),110]      #   a2
               [('7'),123.47]   #   b2
               [('8'),130.81]   #   c3
               [('9'),146.83]   #   d3
               [('0'),164.81]   #   e3
               [('q'),174.61]   #   f3
               [('w'),196]      #   g3
               [('e'),220]      #   a3
               [('r'),246.94]   #   b3
               [('t'),261.63]   #   c4
               [('y'),293.66]   #   d4
               [('u'),359.63]   #   e4
               [('i'),349.23]   #   f4
               [('o'),392]      #   g4
               [('p'),440]      #   a4
               [('a'),493.88]   #   b4
               [('s'),523.25]   #   c5
               [('d'),587.33]   #   d5
               [('f'),659.25]   #   e5
               [('g'),698.46]   #   f5
               [('h'),783.99]   #   g5
               [('j'),880]      #   a5
               [('k'),1760]     #   a6
               [('!'),69.30]    #   c2#
               [('@'),77.78]    #   d2#
               [('$'),92.5]     #   f2#
               [('%'),103.82]   #   g2#
               [('^'),116.54]   #   a2#
               [('*'),138.59]   #   c3#
               [('('),155.56]   #   d3#
               [('Q'),185]      #   f3#
               [('W'),207.65]   #   g3#
               [('E'),233.08]   #   a3#
               [('T'),277.18]   #   c4#
               [('Y'),311.13]   #   d4#
               [('I'),369.99]   #   f4#
               [('O'),415.30]   #   g4#
               [('P'),466.16]   #   a4#
               [('S'),554.37]   #   c5#
               [('D'),622.25]   #   d5#
               [('G'),739.99]   #   f5#
               [('H'),830.61]   #   g5#
               [('J'),932.33]   #   a5#
