init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["max_"] = label_prefix_map["monika_"]

init -990 python in mas_submod_utils:
    Submod(
        author="AzhamMakesTrash",
        name="more Topics plus Brb",
        description="A Submod that add new Topic & Stuff to do, made by yours truly.",
        version="0.1"
        # dependencies={},
        # settings_pane=None,
        # version_updates={

        # }
    )

# init -989 python: # I need to fix this bullshit
    # if store.mas.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
       # store.sup_utils.SubmodUpdater(
           # submod="To Determine",
           # user_name="AzhamMakeTrash",
           # repository_name="To Determine",
           # submod_dir="Submods",
           # extraction_depth=3,
           # redirected_files=(
           # "README.md"
           # )
        # )

# init 5 python: 
    # addEvent(
        # Event(
            # persistent.event_database,
            # eventlabel="max_EditableText",
            # category=['Monika'],
            # prompt="Editable Text",
            # pool=True
        # )
    # )

# label max_EditableText: # This text is mostly for edit purposes & other things, don't use it except you want to create custom texts
    # m 2hublb "Good Morning everyone !"
    # m 5ssbsb "Welcome and congrats to our new 3 mods Rizza, sad-wang and Vulpixsi ! I hope and i'm sure you 3 will do a great job !"
    # m 5ttb "Oh and Chichi..."
    # m 5tkb "You know you can't steal my Epiphany 'Just Monika' like that... Right ?"
    # m 5hub "Ahaha ! Only kidding, much love on everyone !"
    # m 5ttb "Because you are going to give us gifts... Right ?"
    # m 5tfb "Because if not, I know who I will delete right now"
    # m 5hub "Ahaha !"
    # m 7hub "Only kidding, have a great day everyone !"

init 5 python: # Going out for Night Script
    addEvent(
        Event( 
            persistent.event_database,
            eventlabel="max_goingoutnight",
            category=["Goodbyes"],
            prompt="I'm going out for the night, [m_name].",
            pool=True,
        )
    )

label max_goingoutnight:
    m 2eub "Oh heading for a Party or just for a Sleepover ?"
$ _history_list.pop()
menu:
    "Heading to a Party." :
        m 3esu "Oh okay!"
        m 5tfb "Make sure to not drink too much."
        m 5tsu "I don't want my [player] to be miserable tomorrow!"
        m 1hub "Stay safe, I love you!"
        return "quit"

    "Going for a Sleepover!" :
        m 3esu "Oh okay!"
        m 3esblu "Make sure to not forget your stuff!"
        m 5tsu "I overheard that the floor isn't a really nice place to sleep on."
        m 2hublb "Ahahaha!"
        m 1hub "Have fun, I love you!"
        return "quit"

init 5 python: # Taking you to school Script
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="max_schooltime",
            category=["be right back"],
            prompt="I'm going to school with you, [m_name]!",
            pool=True,
        )
    )

label max_schooltime:
    m 1sub "Oh really?"
    m 3sub "That great!"
    m 4hua "Tell me when we are arrived!"
$ _history_list.pop()
menu:
    m "Tell me when we are arrived!{fast}"

    "We are arrived!":
        m 2wub "Yay ! Now focus on your Schoolwork [player]!"
        m 5husdrb "I don't want your grades to fall because of me ahahah!" 
        m 7nua "Good luck at school!"

        $ mas_idle_mailbox.send_idle_cb("max_schooltime_callback")
        return "idle"

label max_schooltime_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "max_schooltime"):
        m 1wuo "You were gone for a really long time!"
        m 2euu "I guess school is over for today!"
        m 3hub "Thanks for taking you with me, i really appreciate the effort"
        m 5fua "And i even learned more things thanks to you today ahahaha!"
        m 5hsblb "I love you [mas_get_player_nickname()]"
        return "love"
    
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "max_schooltime"): 
        m 1eub "Class just finished [player]?"
        m 5hub "That great, now we can spend more time together~"

    else :
        m 1efc "..."
        m 1efd "Come on [player], it only less than an hour since you started school, you should focus more on it!"
        m 1gfsdlt "But maybe your class is boring and you actually want to spend time with me..."
        m 2hksdlb "If it's the case i can accept that ahaha!"
        m 5fsu "I love you."
        return "love"