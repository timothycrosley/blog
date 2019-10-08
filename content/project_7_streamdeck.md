Title: Introducing streamdeck_ui
Date: 2019-10-08 4:30
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-7-streamdeck_ui

[![streamdeck_ui Logo](https://raw.githubusercontent.com/timothycrosley/streamdeck-ui/master/art/logo_large.png)](https://timothycrosley.github.io/streamdeck-ui/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 7/52 |
| Title/Link: | [streamdeck_ui](https://timothycrosley.github.io/streamdeck-ui/) |
| Pitch: | For the first time, use Elgato Stream Deck devices on Linux without needing to code. |
| Read if: | You own or have wanted to own an Elgato Stream Deck device and use Linux. |
| Skip if: | You aren't interested in Stream Decks or other programmable LCD keyboards. |
| Prior Work: | [Python Elgato Streamdeck](https://github.com/abcminiuser/python-elgato-streamdeck), [Coffee2Code Project](https://twitter.com/_Coffee2Code/status/1010652010889310210) |

# In Defense of Saving Seconds

If you haven't seen one before, A Stream Deck is a programmable keyboard, where each key contains an LCD screen.
YouTubers and streamers commonly use it to do such things as trigger tweets, change volume, and switch cameras.

Since the first time I saw someone using a Stream Deck, I wanted one.
I immediately envisioned, all my favorite apps, hot-key combinations, and commands only one physical button push away.
Sure, it's unlikely such a set up would save much time, but it would save some time. And, if it saved just one minute a day, in 10 years, I would have saved two and a half days!
But, it wasn't meant to be, because Stream Deck devices didn't support Linux. And there was no way I was going to stop using Linux.

Being the practical person I am, I didn't give up. I needed that time back.
So, I spent 13 days researching how far others had gotten, and finishing support for seamlessly using Elgato Stream Deck devices on Linux.

Of course, I'm aware that I've almost certainly introduced more work for myself than I could ever possibly save from the device.
I probably would have been better off setting up and memorizing a consistent set of hot-keys.
But, it's hard to underestimate the value of having a tool I utilize every day that symbolizes efficiency at all costs.
It appeals to my programmer sensibilities more than enough to make it all worth it.

# Getting the Stream Deck Working

When I started researching, I was excited to see that 1) this was a somewhat well-beaten path, and 2) no one had "finished" or even gotten close.
That meant I wouldn't have to start from scratch, but there was also still room for me to contribute. It also implied that there was likely demand
from other people for something like this to exist.

No one that I could see had gotten close to giving Linux a similar experience using the Stream Deck as existed on Windows. There was no single application that enabled interacting with the device. Instead, every existing solution required users to code. On the plus side, some great libraries had been written for directly talking to the device. In particular, [this one](https://github.com/abcminiuser/python-elgato-streamdeck), for my favorite language: Python. This library meant, in essence, all I needed to do was build a user interface.
I brushed up on QT, including being introduced to PySide2 for the first time, and got to work. I quickly had something minimal working, but realized how much I missed UI programming, and spent a bit more time to add a few
extra nice to have features.

In the end, you can now [install streamdeck_ui](https://timothycrosley.github.io/streamdeck-ui/#linux-quick-start) on Linux, and use any Elgato Stream Deck without having to write any code at all.
However, if you think of any ways to save just a few more seconds, by writing up some additional logic, I'd be the last one to judge you ;).

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of streamdeck_ui? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
