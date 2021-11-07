# The `aplay` command

`aplay` is a command-line audio player for ALSA(Advanced Linux Sound Architecture) sound card drivers. It supports several file formats and multiple soundcards with multiple devices. It is basically used to play audio on command-line interface. aplay is much the same as arecord only it plays instead of recording. For supported soundfile formats, the sampling rate, bit depth, and so forth can be automatically determined from the soundfile header.

## Syntax:

```
$ aplay [flags] [filename [filename]] ...
```

## Options:

```
-h, –help : Show the help information.
-d, –duration=# : Interrupt after # seconds.
-r, –rate=# : Sampling rate in Hertz. The default rate is 8000 Hertz.
–version : Print current version.
-l, –list-devices : List all soundcards and digital audio devices.
-L, –list-pcms : List all PCMs(Pulse Code Modulation) defined.
-D, –device=NAME : Select PCM by name.
```

Note: This command contain various other options that we normally don’t need. If you want to know more about you can simply run following command on your terminal.

```
aplay --help
```

## Examples :

1. To play audio for only 10 secs at 2500hz frequency.

   ```
   $ aplay -d 10 -r 2500hz sample.mp3
   ```

   > Plays sample.mp3 file for only 10 secs at 2500hz frequency.

2. To play full audio clip at 2500hz frezuency.

   ```
   $ aplay -r 2500hz sample.mp3
   ```

   > Plays sample.mp3 file at 2500hz frezuency.

3. To Display version information.

   ```
   $ aplay --version
   ```

   > Displays version information. For me it shows aplay: vesrion 1.1.0

---
