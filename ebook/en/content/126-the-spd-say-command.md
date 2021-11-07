# The `spd-say` command

`spd-say` sends text-to-speech output request to speech-dispatcher process which handles it
       and ideally outputs the result to the audio system.

## Syntax:

```
$ spd-say [options] "some text"
```

## Options:

```
-r, --rate
       Set the rate of the speech (between -100 and +100, default: 0)

-p, --pitch
       Set the pitch of the speech (between -100 and +100, default: 0)

-i, --volume
       Set the volume (intensity) of the speech (between -100 and +100, default: 0)

-o, --output-module
       Set the output module

-l, --language
       Set the language (iso code)

-t, --voice-type
       Set the preferred voice type  (male1,  male2,  male3,  female1,  female2,  female3,
       child_male, child_female)

-m, --punctuation-mode
       Set the punctuation mode (none, some, all)

-s, --spelling
       Spell the message

-x, --ssml
       Set SSML mode on (default: off)

-e, --pipe-mode
       Pipe from stdin to stdout plus Speech Dispatcher

-P, --priority
       Set  priority  of  the  message  (important, message, text, notification, progress;
       default: text)

-N, --application-name
       Set the application name used to establish the connection to specified string value
       (default: spd-say)

-n, --connection-name
       Set  the connection name used to establish the connection to specified string value
       (default: main)

-w, --wait
       Wait till the message is spoken or discarded

-S, --stop
       Stop speaking the message being spoken in Speech Dispatcher

-C, --cancel
       Cancel all messages in Speech Dispatcher

-v, --version
       Print version and copyright info

-h, --help
       Print this info
```

## Examples :

1. To Play the given text as the sound.

```
$ spd-say "Hello"
```

>Plays "Hello" in sound.
