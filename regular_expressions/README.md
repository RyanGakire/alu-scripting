# ALU - Regular Expressions

This directory contains Ruby exercises for practicing regular expressions.

## Requirements

- Ruby 3.0 or later

## Usage

Run the commands from this directory. Each script accepts its input as the
first command-line argument:

```bash
./0-simply_match_school.rb "School is fun"
./6-phone_number.rb "1234567890"
```

If a script is not executable, run it with Ruby:

```bash
ruby 0-simply_match_school.rb "School is fun"
```

## Exercises

| File | Description |
| --- | --- |
| `0-simply_match_school.rb` | Matches the word `School`. |
| `1-repetition_token_0.rb` | Matches `hb`, followed by 2 to 5 `t` characters, then `n`. |
| `2-repetition_token_1.rb` | Matches `htn` or `hbtn` because the `b` is optional. |
| `3-repetition_token_2.rb` | Matches `hbtn` with one or more `t` characters. |
| `4-repetition_token_3.rb` | Matches `hbtn` with zero or more `t` characters. |
| `5-beginning_and_end.rb` | Matches three-character strings beginning with `h` and ending with `n`. |
| `6-phone_number.rb` | Matches exactly 10 digits. |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts uppercase letter sequences. |
| `8-textme.rb` | Extracts the sender, receiver, and flags from a TextMe log line. |

## TextMe example

`8-textme.rb` can receive a complete log line directly:

```bash
./8-textme.rb 'Feb  1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:+14169955502] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
```

It prints:

```text
+14169955502,+16474951758,-1:0:-1:0:-1
```

It also accepts log lines through standard input:

```bash
cat log.txt | ./8-textme.rb
```
