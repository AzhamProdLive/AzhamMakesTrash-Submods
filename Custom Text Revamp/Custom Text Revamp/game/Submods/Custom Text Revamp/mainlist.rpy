init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_text",
            prompt="Custom Text",
            category=["Custom Text"],
            pool=True,
            unlocked=True
        )
    )

label monika_text:
    m "What do you want me to say, [player]?{nw}"
    $ moniText = mas_input(
            "What do you want me to say, [player]?"
        )
    m "What expression should I do?{nw}"
    
    $ _history_list.pop()

label main_emotionmenu:

    menu:
        m "What expression should I do?{fast}"
        
        "Happy":
            jump happy_menu
        "Sad":
            jump sad_menu
        "Anger":
            jump anger_menu
        "Fear":
            jump fear_menu
        "Love":
            jump love_menu
        "Sparkle":
            jump sparkle_menu
        "Crazy":
            jump crazy_menu
        "Smug":
            jump smug_menu

label happy_menu: #done

    menu: 
        "Happy Default":
            m 1esa "[moniText]"
            return
        
        "Happy + Crossed":
            m 2esu "[moniText]"
            return

        "Happy + Rest & Point + Smile":
            m 3esb "[moniText]"
            return
        
        "Happy + Point Right":
            m 4esa "[moniText]"
            return
        
        "Happy + Leaning + Smile":
            m 5esb "[moniText]"
            return

        "Happy + Down + Smug":
            m 6esu "[moniText]"
            return
        
        "Happy + Down & Point":
            m 7esa "[moniText]"
            return

        "Back":
            jump main_emotionmenu

label sad_menu: #done
    
    menu:
        "Sad Default":
            m 1ekc "[moniText]"
            return
        
        "Sad + Crossed + Small Mouth":
            m 2ekd "[moniText]"
            return
        
        "Sad + Rest & Point + Straight Mouth":
            m 3ekc "[moniText]"
            return

        "Sad + Point + Small Mouth":
            m 4ekd "[moniText]"
            return
        
        "Sad + Leaning + Small Mouth":
            m 5ekd "[moniText]"
            return
        
        "Sad + Down + Straight Mouth":
            m 6ekc "[moniText]"
            return
        
        "Sad + Down & Point + Small Mouth":
            m 7ekd "[moniText]"
            return

        "Intense Emotions":
            jump sadintense_menu
        "Back":
            jump main_emotionmenu

label sadintense_menu: #done

    menu:
        "Crying + Small Mouth":
            m 1dktpd "[moniText]"
            return
        
        "Crying + Look Right":
            m 2rktpc "[moniText]"
            return
        
        "Crying + Rest & Point + Small Mouth":
            m 3rktpd "[moniText]"
            return

        "Crying + Point + Look Right":
            m 4rktpc "[moniText]"
            return

        "Crying + Leaning":
            m 5hktpc "[moniText]"
            return
        
        "Crying + Down + Look Left":
            m 6lktpc "[moniText]"
            return
        
        "Crying + Down & Point":
            m 7ektpc "[moniText]"
            return

        "Normal Emotions":
            jump sad_menu

        "Back":
            jump main_emotionmenu

label anger_menu: #done

    menu:
        "Angry Default":
            m 1ttp "[moniText]"
            return
        
        "Angry + Crossed":
            m 2efp "[moniText]"
            return

        "Angry + Rest & Point + Small Mouth":
            m 3efd "[moniText]"
            return
        
        "Angry + Point + Small Mouth":
            m 4tfd "[moniText]"
            return

        "Angry + Leaning":
            m 5tfp "[moniText]"
            return

        "Angry + Look Left + Down":
            m 6lfc "[moniText]"
            return

        "Angry + Down & Point":
            m 7ffc "[moniText]"
            return

        "Intense Emotions":
            jump angerintense_menu
        "Back":
            jump main_emotionmenu

label angerintense_menu: #done
    #these look goofy ahh
    menu:
        "Pissed Off Default":
            m 1cfc "[moniText]"
            return
        
        "Pissed Off + Crossed + Small Mouth":
            m 2cfd "[moniText]"
            return
        
        "Pissed Off + Down & Point + Grit Teeth":
            m 3cfx "[moniText]"
            return

        "Pissed Off + Point + Screaming":
            m 4cfw "[moniText]"
            return

        "Pissed Off + Leaning + Small Mouth":
            m 5cfd "[moniText]"
            return
        
        "Pissed Off + Down + Small Mouth":
            m 5cfd "[moniText]"
            return
        
        "Pissed Off + Down & Point":
            m 7cfc "[moniText]"
            return

        "Normal Emotions":
            jump anger_menu
        "Back":
            jump main_emotionmenu

label fear_menu: #done

    menu:
        "Nervous Default":
            m 1hksdlb "[moniText]"
            return
        
        "Nervous + Crossed + Sweat":
            m 2lksdlc "[moniText]"
            return
        
        "Nervous + Down & Point + Pout + Sweat":
            m 3lksdlp "[moniText]"
            return

        "Nervous + Point + Small Mouth + Sweat":
            m 4lksdld "[moniText]"
            return

        "Nervous + Leaning + Straight Mouth + Sweat":
            m 5dksdrc "[moniText]"
            return

        "Nervous + Down + Straight Mouth + Sweat":
            m 6dksdlc "[moniText]"
            return
        
        "Nervous + Down & Point + Look Right + Sweat":
            m 7rksdla "[moniText]"
            return

        "Intense Emotions":
            jump fearintense_menu
        "Back":
            jump main_emotionmenu

label fearintense_menu: #done

    menu:
        "Scared Default":
            m 1wksdlx "[moniText]"
            return

        "Scared + Crossed":
            m 2wksdlx "[moniText]"
            return
        
        "Scared + Rest & Point + Gasp + Sweat":
            m 3wksdlo "[moniText]"
            return

        "Scared + Point + Straight Mouth + Sweat":
            m 4wksdlc "[moniText]"
            return
        
        "Scared + Leaning + Straight Mouth + Sweat":
            m 5cksdlc "[moniText]"
            return
        
        "Scared + Down + Small Mouth":
            m 6ckd "[moniText]"
            return

        "Scared + Down & Point + Straight Mouth + Sweat":
            m 7cksdlc "[moniText]"
            return
            
        "Normal Emotions":
            jump fear_menu
        "Back":
            jump main_emotionmenu

label love_menu: #done

    menu:
        "Soft Default":
            m 1fkblb "[moniText]"
            return

        "Soft + Smile":
            m 1fkbsb "[moniText]"
            return
        
        "Soft + Smile + Blush":
            m 1fubsb "[moniText]"
            return

        "Soft + Leaning + Blush":
            m 5fubfa "[moniText]"
            return
        
        "Soft + Leaning + Blush + Smile":
            m 5fubfb "[moniText]"
            return

        "Soft + Crossed + Blush":
            m 2fkbla "[moniText]"
            return

        "Soft + Crossed + Blush + Smile":
            m 2fkblb "[moniText]"
            return

        "Back":
            jump main_emotionmenu

label loveintense_menu: #todo

    menu:
        "Coming soon...":
            return

        "Normal Emotions":
            jump love_menu
        "Back":
            jump main_emotionmenu

label sparkle_menu: #done

    menu:
        "Sparkle Smile":
            m 1sub "[moniText]"
            return
        
        "Sparkle + Crossed + Surprised":
            m 2subld "[moniText]"
            return

        "Sparkle + Rest & Point + Smile":
            m 3sub "[moniText]"
            return

        "Sparkle + Point Right":
            m 4suu "[moniText]"
            return

        "Sparkle + Leaning + Smile":
            m 5skb "[moniText]"
            return

        "Sparkle + Down + Smile":
            m 6skb "[moniText]"
            return
        
        "Sparkle + Furrowed + Down & Point + Smile":
            m 7sfb "[moniText]"
            return

        "Back":
            jump main_emotionmenu

label crazy_menu: #done

    menu:
        "Crazy Default":
            m 1cua "[moniText]"
            return

        "Crazy + Smile":
            m 1cub "[moniText]"
            return

        "Crazy + Smile + Blush":
            m 1cublb "[moniText]"
            return
        
        "Crazy + Blush + Down":
            m 6csbla "[moniText]"
            return
        
        "Crazy + Point + Smile":
            m 7csb "[moniText]"
            return

        "Crazy + Crossed":
            m 2csa "[moniText]"
            return

        "Crazy + Smile + Crossed":
            m 2csb "[moniText]"
            return

        "Back":
            jump main_emotionmenu

label crazyintense_menu: #todo

    menu:
        "Coming Soon...":
            return

        "Normal Emotions":
            jump crazy_menu
        "Back":
            jump main_emotionmenu

label smug_menu: #done

    menu:
        "Smug Default":
            m 1tsu "[moniText]"
            return

        "Smug + Crossed + Smile":
            m 2tsb "[moniText]"
            return

        "Smug + Rest & Point + Blush":
            m 3tsblu "[moniText]"
            return
        
        "Smug + Point + Smile":
            m 4tsb "[moniText]"
            return

        "Smug + Leaning + Blush":
            m 5tsbsu "[moniText]"
            return

        "Smug + Down + Blush + Smile":
            m 6tsbsb "[moniText]"
            return
        
        "Smug + Down + Blush":
            m 7tsblu "[moniText]"
            return

        "Back":
            jump main_emotionmenu

