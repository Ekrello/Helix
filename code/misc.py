def helpmusic():
    helpmsg1 = "```"
    helpmsg1 += "===Music===\n"
    helpmsg1 += "/play [song name or url]\n"
    helpmsg1 += "/search [song name]\n"
    helpmsg1 += "/volume [number]   <--Volume control\n"
    helpmsg1 += "/stream            <--Play a stream\n"
    helpmsg1 += "/skip              <--Skips the song?\n"
    helpmsg1 += "/pause             <--Pauses the song\n"
    helpmsg1 += "/resume            <--Resumes the song\n"
    helpmsg1 += "/playlist          <--Shows current playlist\n"
    helpmsg1 += "/np                <--Shows whats Now Playing\n"
    helpmsg1 += "/shuffle           <--Shuffles the playlist\n"
    helpmsg1 += "/getout            <--Disconnects from the current voice channel\n"
    helpmsg1 += "/spawn             <--Joins the voice channel you are in\n"
    helpmsg1 += "/clear             <--Clear the playlsist (dont be a dick)\n"
    helpmsg1 += "/supported         <--All the links Toasty supports\n"
    helpmsg1 += "/electronic        <--Creates a playlist of electronic songs\n"
    helpmsg1 += "/rock              <--Creates a playlist of rock songs\n"
    helpmsg1 += "/rap               <--Creates a playlist of rap songs\n"
    helpmsg1 += "/retro             <--Creates a playlist of retro songs\n"
    helpmsg1 += "/metal             <--Creates a playlist of metal songs\n"
    helpmsg1 += "/jazz              <--Creates a playlist of jazz songs\n"
    helpmsg1 += "/classical         <--Creates a playlist of classical songs\n"
    helpmsg1 += "/japanese          <--Creates a playlist of japanese songs\n"
    helpmsg1 += "/add               <--Create a playlist made from urls on your pastebin\n"
    helpmsg1 += "/loop [number]     <--Loop a set song a set amount of times\n"
    helpmsg1 += "```"
    return helpmsg1


def helputility():
    helpmsg2 = "```"
    helpmsg2 += "===Utility===\n"
    helpmsg2 += "/help              <--This message\n"
    helpmsg2 += "/id                <--Get your ID\n"
    helpmsg2 += "/bug               <--use this to report bugs\n"
    helpmsg2 += "/join              <--Add me to your server or join my server\n"
    helpmsg2 += "/donate            <--Donate to the project and help keep the bot alive\n"
    helpmsg2 += "/feature           <--Request a feature to be added to toasty\n"
    helpmsg2 += "/info              <--General Information about the bot\n"
    helpmsg2 += "/updatelog         <--Information about what was in the last update\n"
    helpmsg2 += "/ping              <--Ping the bot\n"
    helpmsg2 += "/google            <--Google Search\n"
    helpmsg2 += "/lmgtfy            <--Legacy Google Search -- lmgtfy.com\n"
    helpmsg2 += "/urban             <--Urban Dictionary\n"
    helpmsg2 += "/gif[word          <--Giphy\n"
    helpmsg2 += "/cat               <--I want to see cats, and i want them now\n"
    helpmsg2 += "/dog               <--Give me my doggo\n"
    helpmsg2 += "/server            <--Server Info\n"
    helpmsg2 += "```"
    return helpmsg2


def helpadmin():
    helpmsg3 = "```"
    helpmsg3 += "===Server Admin Utilities===\n"
    helpmsg3 += "/apocalypse        <--Delete all messages in the current channel\n"
    helpmsg3 += "/listids           <--Get all the IDs from the server\n"
    helpmsg3 += "/clean             <--Remove all Toaster related spam\n"
    helpmsg3 += "/kick              <--Kick a mentioned user\n"
    helpmsg3 += "/ban               <--Ban a mentioned user\n"
    helpmsg3 += "/leaveserver       <--Make the bot leave the server\n"
    helpmsg3 += "```"
    return helpmsg3


def helpchat():
    helpmsg4 = "```"
    helpmsg4 += "===chat===\n"
    helpmsg4 += "/toast             <--Cleverbot\n"
    helpmsg4 += "/savage            <--Insults\n"
    helpmsg4 += "/compliments       <--Compliments\n"
    helpmsg4 += "/vicky             <--Victorian insults\n"
    helpmsg4 += "/8ball[question]   <--Magic 8-ball\n"
    helpmsg4 += "/shitpost          <--A random shitpost message\n"
    helpmsg4 += "/flip              <--Flip coins...and something else\n"
    helpmsg4 += "/knock             <--knock knock\n"
    helpmsg4 += "/weather [location]<--weather where you are\n"
    helpmsg4 += "/doge [words]      <--generate a doge meme\n"
    helpmsg4 += "/echo [text]       <--echo what you said\n"
    helpmsg4 += "```"
    return helpmsg4


def helpdonate():
    helpmsg5 = "**Oh cool youre a donator ^-^**\n **Soon youll get awesome features that only donators can use**"


def patebin(link):
    import urllib.request
    from bs4 import BeautifulSoup
    link = link.replace(".com/", ".com/raw/")
    try:
        text = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(text, "html.parser")
    except:
        return
    text = soup.get_text()
    text = text.replace("<bound method Tag.get_text of ", "")
    text = text.replace(">", "")
    print("")
    print("")
    print("")
    return text


def shitpost():
    import random
    text = """UNROLL THE TADPOLE OSfrog UNCLOG THE FROG OSfrog UNLOAD THE TOAD OSfrog UNINHIBIT THE RIBBIT OSfrog UNSTICK THE LICK OSfrog UNIMPRISON THE AMPHIBIAN OSfrog UNMUTE THE NEWT OSfrog UNBENCH THE KENCH OSfrog PERMIT THE KERMIT OSfrog DEFOG THE POLLIWOG OSfrog
O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA
¦---¦Lets build a ladder¦---¦
( ?° ?? ?°) ?CLOWN FIESTA ( ?° ?? ?°)
Sodium, atomic number 11, was first isolated by Humphry Davy in 1807. A chemical component of salt, he named it Na in honor of the saltiest region on earth, North America.
MingLee I MingLee KNOW MingLee WHEN MingLee THAT MingLee HOTLINE MingLee MING MingLee THAT MingLee CAN MingLee ONLY MingLee MING MingLee ONE MingLee LEE MingLee YOU MingLee USED MingLee TO MingLee MingLee CALL MingLee ME MingLee ON MingLee MY MingLee CELLPHONE MingLee
EleGiggle MY BELLY IS HUGE EleGiggle MY BRAIN HAS DELAY EleGiggle YOU GUESSED IT RIGHT EleGiggle I'M FROM NA. EleGiggle
High in orbit, the Gitraktmaet motherships descend upon the Earth. They prepare to enslave the world and mine it for all its salt, but the scanners detect an abnormally high concentration inside a tiny shack in Greece. The invasion won't be necessary. "Lock onto him with the RNG disruptor," says the captain, greedily. "Soon we shall have all the salt we need."
( ?° ?? ?°) OVERCONFIDENCE IS A SLOW AND INSIDIOUS KILLER ( ?° ?? ?°)
YESTERDAY YOU SAID TOMMOROW, Don't let your dreams be memes, Don't meme your dreams be beams, Jet fuel won't melt tomorrow's memes, DON'T LET YOUR STEEL MEMES BE JET DREAMS
???????????????????? good shit go?? sHit?? thats ? some good????shit right????th ?? ere?????? right?there ??if i do ?a? so my self ?? i say so ?? thats what im talking about right there right there (chorus: ????? ?????) mMMMM???? ???? ???O0??OOOOO???Oooo??????????? ???? ?? ?? ?? ?? ?? ?? ????Good shit
PogChamp PogChamp HOLD CTRL AND TYPE "WTF" FOR F???????? ????F PogChamp PogChamp
I sexually Identify as an the sun. Ever since I was a boy I dreamed of slamming hydrogen isotopes into each other to make helium & light and send it throught the galaxy. People say to me that a person being a star is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon inflate me with hydrogen and raise my temperature to over 6000 °C. From now on I want you guys to call me “Sol” and respect my right to give you vitamin D and probably sunburns. If you can’t accept me you’re a fusionphobe and need to check your astral privilege. Thank you for being so understanding.
Hello Kripparrian, this is Reginald. It has come to my attention that you went 0-3 in Hearthstone arena. This is completely unacceptable and detrimental to the image of Team Solo Mid. Remove any and all affiliation with TSM and "BayLife" or I will be forced to call the 0-3 Police.
I WILL NOW TRANSFORM THIS HUMAN INTO A CAT?( ?° ?? ?° )?--? -> -> -> Kappa Keepo CoolCat
4Head [_¯$_¯(_¯5_¯)_¯$_¯] Look subs, I have more money than you 4Head
? amazW ? krippW ? trumpW ? reynadW ? kolentoW ? bajW ? dewW ? emjaneW ? forsenW ? krippW ? loidW ? mitchW ? reckW ? sodaW ? taymooW ? PLEB TEST PASSED.
---¦( ?° ??+--- HEY KIDS DO YOU WANT SOME DANK MEMES?
8=====> Only the chosen one can hold his donger ? PogChamp ?
?  ? ° ? ? ¸. ¸  ?  :.  . • ? ° ?  .  * . .  ¸ .   °  ¸. * ? ¸ . ...somewhere   ° ? °  ¸. ? ¸ .  ? ° :.  . • °   .  * :. .in a parallel universe* ? ¸     ° ? °?  . * ¸.   ? ? ° . .    . ? °?  . * ? ¸ ..Reynad...° ? ? °? ¸ .   ? ° :.  . • ? ° ?  .  * Isn't salty ? ? °? ¸ .   ? °
BabyRage NEVER LUCKY BabyRage
LETS BUILD A RAINBOW CHAT! ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
Eeeyoo I had the most amazing sex with this girl last night. It was so good I came in 15 seconds and as I turned to look at her out of embarrassment, she put her lips to my ear and whispered "at least you lasted longer than NA at worlds" 4Head
(¬ ?? ?? ??) Alright students, how often is Kripp lucky? ???????? Call on me! (¬ ?? ?? ??)  Yes little Dong?  ???????? Kripp is never lucky, sir! (¬ ?? ?? ??)   Wrong, Kripp is lucky a reasonable amount of time.    Come see me after class for your punishment . ?¬ ?? ?? ???
?? ? ?°? ??? ? ?° ??¤=[———— Hello. My name is Inigo Dongtoya. You killed my Kappa. Prepare to die.
Hello Reynad, big fan here trying to fulfill my dreams of being an industrial vacuum for constipated hospital patients, any tips on sucking ass?
(¯?L?¯? ?) This is the 0-3 Police, You're coming with us Kripp. (¯?L?¯? ?)
Hey guys. This is my very first copy pasta and I am really nervous about pasting it because if it does not get copy pasta then I will have much embarrassment. I've have thinking about it for a couple of nights now, but here it is!.
One time my mother called me a son of a bitch, so I hit her because no one talks trash about my mother, then I hit myself because no one hits my mother, she then hit me because no one hits her son and then hit herself because no one hits me, so I hit her because no one hits my mother. cant stop me
Hi, I am an Albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer. Please be so kind to delete one of your important files yourself and then forward me other users. Many thanks for your cooperation! Best regards, Albanian virus
? Obesity ? ???? ? Laziness ? Stupidity ? ?? ? McDonald's ? Donald Trump ? $70k College ? Bad healthcare ? Bad food ? Bad music ? Fahrenheit ? Pounds ? Inches ? AMERICAN TEST PASSED
Europe was founded in 1848 by Walker Texas Ranger when he rode a horse across the Atlantic, he called it "Eastern USA" which was eventually abbreviated as just "EU"
If the human body is 75% water, how can you be 100% salt? Kappa
?HELLO AM 48 YEAR MAN FROM SOMALIA. SORRY FOR BAD ENGLAND. I SELLED MY WIFE FOR INTERNET CONNECTION FOR PLAY "hearth stone" AND I WANT TO BECOME THE GOODEST PLAYER LIKE YOU I PLAY WITH 400 PING ON BRAZIL SERVER AND I AM RANK 23 ALREADY PLS NO COPY PASTE MY STORY
VoHiYo THATS VoHiYo THE VoHiYo WRONG VoHiYo HOLE VoHiYo ONII-CHAN VoHiYo KYAAAAH VoHiYo
Born too late to explore the Earth, born too early to explore the universe, born perfectly to explore dank memes ? ? ? ? ??
HEY  DOUBLELIFT,  I’M  TRYING  TO  LEARN  TO  PLAY  SHACO.  I  JUST  HAVE  A  QUESTION  ABOUT  THE  SKILL  BUILD:  SHOULD  I  MAX  BACKSTAB  LIKE  YOU  BACKSTABBED  CLG,  DECEIVE  LIKE  YOU  DECEIVED  CLG,  OR  HALLUCINATE  LIKE  YOU  MADE  CLG  HALLUCINATE  ABOUT  HAVING  A  CHANCE  AT  WINNING  ANOTHER  TOURNAMENT
KKona HEY KKona FORSEN KKona HOW KKona ABOUT KKona SOME KKona BROTHERMAN KKona BILL KKona
(?°?°)?? ??? FLIP THAT TABLE. ??? ? ?(°?°?) FLIP THIS TABLE. ??? ? \\('0')// ? ??? FLIP ALL THE TABLES ?_? Son... ?_? Put. ?__? The tables. ?___? Back. (?°-°)???? (?°?°)?? ??? NEVER!!!!
<:::::[]=¤??????? My name is Maximus Kappacus Spamicus, commander of the Armies of the Twitch, General of the PJSalt Legions, loyal servant to the true Emperor Kripparrian. Father to a banned son, and husband to a banned wife. I will slay all moderinos, whether in this chat or the next. <:::::[]=¤???????
<message deleted: memes too dank>
If 700,000 people die in hospitals every year. Why don't we close down these hospitals and prevent those deaths? (? ?° ?? ?°)?
Can we all stop hating on Amaz for a moment? I mean, yes, he is a colossal fake cunt, moneysucking parasite, and selfish prick. But he is one of the few representations of the gay community in Hearthstone.
??? ??? ? ??????-???? ??? ??????????? ????? ???????? ??????? ??? ?? ?? ?????? ???? ????. ??? ?????? ??? ??? $4.99 ?? ?? s?. ????? ??? s????? ???s???? ??????? ?????s ?? ???s??????? ??? ??? ????.
( ?° ?? ( ?° ?? ( ?° ?? ?°) YOU CAME TO THE WRONG CIRCUS ( ?° ?? ( ?° ?? ( ?° ?? ?°)
TBTacoLeft TBTacoRight WHAT IS INSIDE THAT TACO  TBTacoLeft TBCheesePull 0  TBCheesePull TBTacoRight OH NO IT'S REYNAD'S TOURNAMENT WINS LUL
Hi Imaqtpie. I noticed that in your games you utilize Kog’Maws passive A LOT, but when I watch LCS players I see them go an ENTIRE teamfight without using their passive even ONCE. Are they playing the champion to its full potential or are you?
<(°) Le budget Toucan has arrived
( ?° ?? ?°) When i hold my mouse-cursor over reynads mouse-cursor, it feels like i am holding hands with him ( ?° ?? ?°)
Year 2020 Jared loses a game in D3 , but he manages to think positively... If something is wrong, fix it if you can. But train yourself not to worry. Worry never fixes anything... he continues to lose another game.... I like the dreams of the future better than the history of the past... is what he tells himself... he loses another one ... and reaches for the glock
ASCENDED invisible spam ?? ???? ? ? ? ??????? ? ? ? ? ? ? ? ???? ?? ?? ??????? ? ?????? ? ? ? ? ? ?? ??? ?? ???? ? ? ? ? ???? ? ? ? ??????? ? ? ? ? ? ? ? ???? ?? ?? ??????? ? ?????? ? ? ? ? ? ?? ??? ?? ???? ? ? ? ? ???? ? ? ? ??????? ? ? ? ? ? ? ? ???? ?? ?? ??????? ? ?????? ? ? ? ? ? ?? ??? ?? ???? ? ? ? ? ???? ? ? ? ??????? ? ? ? ? ? ? ? ???? ?? ?? ??????? ? ?????? ? ? ? ? ? ?? ??? ?? ???? ? ? PogChamp
( ?° ?? ?°) Every 60 seconds in Africa, a minute passes. Together we can stop this. Please spread the word ( ?° ?? ?°)
Hello Miguel Santander, this is your cat, Mellow Cat, I heard that you were complaining about my excesive meowing. I dont complain about having to hear you talk to yourself for 8 hours while playing that stupid game so I expect the same. Come here and feed me scrub CoolCat
They say 9 out of 10 twitch users are dumb. I'm so glad to be in the other 1 percent
If you are reading this, WAKE UP. You are in a simulation. Don't you see it? The same responses repeating in chat? Its because the computer only has a set number of lines. Wake up before its too late!
~ Kreygasm ~ ~ Kreygasm ~ ~ Kreygasm ~ DUDUDUDUDUDU ~ Kreygasm~ ~ Kreygasm ~ ~ Kreygasm ~
???????·????-??I'VE GOT THE STREAM IN MY SIGHTS
Hello Kripp, your stream has changed my life completely. I suffer from severe NaCl (salt) deficiency disorder. I had to visit the hospital 5 times a week for salt injections. However, watching your stream supplies me enough salt through the screen. You saved me money time and effort. I can't thank you enough. I owe u my life.
“This guy's vape is CRAZY!” VapeNation “My vape can't win against a rip like that” VapeNation "He NEEDED precisely those two clouds to win" VapeNation “He ripped the only vape that could beat me” VapeNation "He ripped the perfect vapes" VapeNation “There was nothing I could do” VapeNation “I vaped that perfectly” VapeNation
I'm SICK of STREAMERS referring to all us all as "Twitch Chat" as if we're some sort of hivemind. I am NOT a DRONE. I AM AN INDIVIDUAL!
¦- OSfrog -¦ This frog's head just got stuck on this ladder. To make him feel better, enslave his frog brothers too by spamming this.
( ?° ??? ?°) OVERCLOWNFIDENCE IS A SLOW AND HILARIOUS KILLER ( ?° ??? ?°)
+( ° ???°)+Born too late to explore the Earth, born too soon to explore the Galaxy. Born just in time to TAKE THE PLEB TEST! +( ° ???°)+ ? amazW ? krippW ? trumpW ? reynadW ? kolentoW ? bajW ? dewW ? emjaneW ? forsenW ? krippW ? loidW ? mitchW ? reckW ? sodaW ? taymooW ? PLEB TEST PASSED
DIG is 0-2 down to TIP, in champ select for their next game -"If only QT was here" says Kiwi -Smoke appears and out steps Imaqtpie -He knocks out CoreJJ and instalocks Quinn, screaming 'SQUAAK!' - QT feeds his ass off and DIG lose 0-3
When jon lenon was 10 his teacher askd "what do u wana do when u are adult?" and jon lenon said "hapy". the teacher said "u didn't understand question" and lenon said "u dont understand life.". The teacher was alber Einstein, retweet if u beliv in god
This is an automated message from Twitch TV. We have been experiencing technical difficulties related to the Kappa face. Please confirm that your Kappa face is working properly.
The year is 2027, Jared has just returned from his third tour in North Korea. Each time he fired his rifle he whispered the same word, "/ff". He looks down to the 9mm in his belt and dreams of seeing imaqtpie and Dom one last time, one final "/ff'
OpieOP EU is so ba... OpieOP wait let me take a breath OpieOP EU is s... OpieOP i need to take another one OpieOP fk give me another burger OpieOP
Hi, my name is Bill Gates and today I’ll teach you how to count to ten: 1, 2, 3, 95, 98, NT, 2000, XP, Vista, 7, 8, 10
VapeNation VAPE ME UP VapeNation VAPE ME UP INSIDE VapeNation CAN'T VAPE UP VapeNation VAPE ME UP INSIDE VapeNation VAPE MEEEEE VapeNation CALL MY NAME AND VAPE ME VapeNation
I was offered sex today, with a 21 year old girl. In exchange for that, I was supposed to advertise some kind of e-betting website to my friends. Of course I declined because I am a person of high moral standards with a strong willpower. Just as strong as Ebettle, the best betting website on the internet. Now available for children.
Jared, jumping for joy at the site of an easy victory with QT thought he was back with the crew. Little did he know QT was devising a cunning plan to demote Jared back to Diamond 3. Boom, like a shot in the dark, an instant 4 man surrender stole the wind right out of Jared. Jared glanced over to his 9mm, knowing one day he will have his chance to right these wrongs.
"So my girlfriend the other day asked if she could roleplay as a 14 year old while we were having sex. I was like what the fuck? That shit's gross. You're gonna be 14 in like two years anyways." - Krepo 2016
?? ??????? ??? ???? ???? ????s??????. ?? ????? ??? s??????s ?????? ??? ??????. ?? ???????? ??? ???? ?? T???? ??? ???s. ?? ?x???? ??? s??? ?? ??? s???s ?????. ????! ??s??! ???? s??? ???s? ??? ?? ??? s???? ?? ?????! s???????? ???s ?? ??????? ?? ?????! K????, ????s ?????!
10% luck, 20% skill, 15% slowly ranking uphill, 5% topdeck, 50% pace or just 100% reason to go for the face SMOrc
I sexually Identify as VapeNation . Ever since I was a boy I dreamed of filling the air with the fattest rips. People say to me that a person being VapeNation is Impossible and I’m *** retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install cloudchasers, coils, and a battery on my body for the perfect vape. From now on I want you guys to call me “Lit” and respect my right to rip the fattest vapes. If you can’t accept me you’re a vapiphobe and need to check your VapeNation privileges
(n ?° ?? ?°)?? This is Wildcard Region Police, NA you are coming with us (n ?° ?? ?°)??
?¯? L?¯?? This is Blizzard, Forsen. We've detected reduced gaming time of our game, Hearth of Stone from you and therefore we reduced your RNG as penalty. ?¯? L?¯??
Hey Reynad you're so salty, if you touched a slug it would die
Please do not copy and paste this copypasta. It is my original copypasta and is protected by copyright law. If I see anyone pasting my intellectual property without permission, a navy seal trained in gorilla warfare will smite you.
? º??º ? Minions, (? •`_•´)? servants, <:::::[]=¤??????? soldiers of the cold dark, obey the call of ( ????????) Kripp'Thuzad ( ????????)!!!
I am a dog being raised by a very loving family. Or at least I was, until a balding romanian gypsy kidnapped me from my home. Now he doesn't let me go outside and doesn't feed me. Every time I try to tell him I am hungry he puts green leaves in my bowl and says doggies can be vegan too if they try hard enough. I believe this man is mentally disabled. Please send help.  OhMyDog
? Not REKT ? REKT ? REKTangle ? SHREKT ? REKT-it Ralph ? Total REKTall ? The Lord of the REKT ? The Usual SusREKTs ? North by NorthREKT ? REKT to the Future ? Once Upon a Time in the REKT ? The Good, the Bad, and the REKT ? LawREKT of Arabia ? Tyrannosaurus REKT ? eREKTile dysfunction
Kappa FEELS Kappa GOOD Kappa TO Kappa BE Kappa A Kappa PLEB Kappa
@Imaqtpie, I hear there is a gaming retirement home if you're looking for round the clock support. It's called TSM house EleGiggle
LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself LE SWARM HAS ARRIVED bUrself BZZZ BZZZ bUrself
Devlinate: Kaiser_HS: snny_: DONT COPY PASTE THE NAME WHEN U COPY PASTE FailFish
?¦?? TOTEMIC MIGHT ?¦??
(•?•) Daddy, is it true as the legend says. That Kripparrian is NEVER lucky? ( ?°?????° ) Yes little dong. The legend holds true even to this day.
BibleThump Andrey Yanuk otherwise known as Reynad has passed away this Saturday's afternoon. He was ambushed by a group of dongers in an alley, and stabbed with a kniferino made out of a salt shaker. His last words were "please use the code "Tempo" to save 3% off the funeral costs and bury me in my tempostorm tshirt". Rest in peace pepperoni cappuccino pistachio bro. You shall be missed. Please no copy pasterino cappuccino
I'm not allowed to take sleep inducement medication, because of a previous addictions to psychoactive drugs. So, my doctor instead prescribed 1 hour of Trump's stream per evening. Kappa
This is Gambit ? º??º? º??º( ?° ? ? ?? ? °)º??º ?º??º ? 5 MEN 9 EYEBROWS , 1 DREAM
ResidentSleeper "Alright, rogue, I guess" ResidentSleeper "Haven't picked mage in a while, let's go mage ResidentSleeper "Paladin isn't that good, but alright" ResidentSleeper
The opponent mulligans his cards. "Oh my god dude, are you kidding me?" says Kripp. The opponent plays a 2 drop. "Seriously dude? This is crazy." The opponent draws a card at the start of their turn. "No fckin way dude, I can't beat that." The opponent hero powers. "This is some crazy RNG bullshit" says Kripp.
This is an automatic message from Amaz. I've lost some of my viewbots. If you are a viewbot, please type MrDestructoid in comments so then I can count you all. Thank you.
4Head Hey Europoops, who built the statue of liberty? NOT YOU EleGiggle STAY POOR EU EleGiggle
Jared shuffles to his locker wiping a tear from his eye. He looks over his shoulder to see DOM and QT, the jock E-Athlete bullies, laughing at him and his wedgie. Jared clinches his fist in rage knowing that soon the time would come, he will show them...
It was dinner time in the Cloud Nein Gaymer house. Zachary “Sneaky” Scuderi dishes up a steaming plate of pasta when he realizes he forgot the meat. William “Meteos” Hartman looks up from his plate with a gleam in his eye. “I got the meat right here for you baby.” Lubing up with Marinara Sauce, Meteos begins to pound his sausage into sneaky’s lightly buttered dinner roll. With a scream of delight Meat-eos releases his load calling an end to another successful team dinner.
,/?/\?? KKona ??/\? \ Spiderman Bill makes his web on the hill ,/?/\?? KKona ??/\? \
Hey Kripp, mom here, my 13 year old son wants 5 dollars so he can "subscribe". I dont know what that is, but a quick Google search shows Kripp subscribers are linked with NaCL overdose disorder. Can you explain this? - Sincerely, a concerned parent
Hey mods I just wanted to congratulate you all and give proper respect for keeping our chats safe from the evils of Twitch, the spammers, and sexual predators. Without you and your methods, which have no affiliation to the leading German political party within the time frame of World War 2, we would not be able to enjoy a fun, clean environment in which we can enrich ourselves with game knowledge and truly become one as a great family for the greater good of internet chatrooms. Again, I would like to say you have done a wonderful job and hope to see you all keep up the great work.
Jared wakes up in the middle of the night gasping for breath. The moon shines high in the starless sky its light upon Jared. It illuminates his, pale almost ghostly face, he is sweating yet he feels so cold. From his lips only one word is whispered "Diamond III" he shivers for this word is a mortal reminder of his haunting nightmare. He tries to calm himself reassuring it was all but a bad dream. He looks up, a surrender vote blinking in the dark, and in the background qtpies maniacal laugh
PogChamp I'M GOING UP THE CHAT ELEVATOR PogChamp I'M GONNA BE FIRST TO ARRIVE PogChamp
FeelsBadMan    ?' ?'\????\ qt's stream ends, so does my life FeelsBadMan    ?' ?'\????\
Pupparrian scampers excitedly as Kripp carries the new bird cage. "Here you go, Birdarrian," says Kripp as he hangs the cage in the office. Unfortunately, Pupparian's joyful romping caused kripp to stumble, the cage bursting open and Birdarrian falling helplessly into the merciless jaws of the paper shredder sitting below the cage. "Oh no," gasps Kripp, "I forgot about shredder placement!"
Hello Kripparian. Its Becky from the Sesame Street Celebrity Recruitment Department. Although "E-Sports" has indeed become mainstream, we unfortunately have declined your application to be on an episode of Sesame Street. We have already filmed the episode where "K" is the letter of the day. Thank you for your interest.
Hello Kripp, I am a 14 year old boy from Canada. I played you today in arena and I won, I was excited to beat a famous player like you! I opened your stream, and I felt bad because you said I played badly and won because of luck. Please say you're sorry or I'll never play Hearthstone again. Please no copy pasterino 10th graderino
nl_Kripp can you stop it with all the salt? I was trapped in a salt mine for 3 days straight without any water or food. I only survived by drinking my own urine and eating my toes. Every time I see you spitting salt everywhere it gives me terrible PTSD flashbacks. Thanks.
Hello, I am currently 15 years old and I want to become a walrus. I know there's a million people out there just like me, but I promise you I'm different. On December 14th, I'm moving to Antarctica; home of the greatest walri. I've already cut off my arms, and now slide on my stomach everywhere I go as training. I may not be a walrus yet, but I promise you if you give me a chance and the support I need, I will become the greatest walrus ever. Thank you all.
?-???_?(+???)?_???-? "YOU'LL NEVER TAKE ME ALIVE MODS!"
EU SwiftRage )))) NotLikeThis (((( BabyRage NA
MingLee SINGLEE MingLee AND MingLee READY MingLee TO MingLee MINGLEE MingLee
No, fellow Twitch chat community member, I will NOT press 1, spam K?ppa, hold my donger, aggravate mods, or copy paste your messages. This is a community of upstanding individuals, such as myself, who wish to keep this chat in a state of peace and clarity.
( ????????) Back in my day copying a message took skill. Now the chat stops moving when you scroll up. Disrespectful kids and their technology. ( ????????)
GORGEOUS TONE OF GRAY ? Kappa TIMELESS DESIGN ? Kappa THE ORIGINAL KING OF THE EMOTES ? Kappa LOTS OF ADORABLE VERSIONS ? KappaPride KappaClaus KappaRoss MUST BE Kappa ? Kappa
HEY BALLS, I’M TRYING TO LEARN TO PLAY DARIUS. I JUST HAVE A QUESTION ABOUT THE SKILL BUILD: SHOULD I MAX DECIMATE LIKE YOU DECIMATED  FNATIC, CRIPPLING  STRIKE  LIKE  YOU  CRIPPLED  FNATIC'S  CHANCES  OF  GETTING  OUT  OF  GROUPS,OR  APPREHEND  LIKE  YOU  APPREHENDED  ALL  FIVE  OF  FNATIC  FOR  A  PENTAKILL.
UPLOADING VIRUS EXE ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦] 98%
I like how StrifeCro doesn't realize that all his viewers are me on different accounts. Dont believe me? watch me post this on my other accounts
forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace forsenX WutFace
Guys please stop spamming. My dog, Bernard, looked at my chat and got so dizzy because of the spam that he fell down and hit his noggin right on his food bowl! He couldn't talk for hours. Please stop spamming, for Bernard.
You notice a wall of text in twitch chat and your hand instinctively goes to the mouse. You scroll up to stop the chat elevator and read the pasta, indulging in its delights... You soon realize that this pasta conveys no information nor is particularly witty or funny. Nevertheless, you drag your mouse across, hit Ctrl+C, then Ctrl+V and press Enter
M? ???? ?? 20 ????s ???? ?? ? ???? ???. I ?????? ?? ??? ?????? ??? ??? ??? ?????s ??????? ??? ??s???? ?? ??? ????????. B?? ?? ????? s???? ?s?'? ?s ?????? ?s ?????? ???????.
Hey Kripp, its Chad from the college football team, how you been bro? I see you're still playing video games some things never change! Hey are you still playing the wizard of warcraft game? I never had time for video games I was too busy playing football and going to frat parties. Anyways good seeing you bro,call me and we can hit the clubs.
deIlluminati DON'T deIlluminati MIND deIlluminati ME deIlluminati JUST deIlluminati PROMOTING deIlluminati THE deIlluminati NEW deIlluminati WORLD deIlluminati ORDER deIlluminati
??????ATTENTION 2003 KIDS??????!!! This ?? is the last year of being a kid ??????! Because NEXT ??YEAR! We gon be T33N4G3RS??????!! PARTYING ???? DRINKING ???????? MAKING OUT AND SEX ?????? PERIODS ???? HEARTBREAKS ???? MIDDLE SCHOOL SOPHOMORES (7TH GRADE)
The year is 2129; humans can only communicate through increasingly garbled copy-pasta. A man approaches and says "ire: ¦¦¦ 10 stroke dick ff ? EKT ? ? ¸. ?" In confusion, I reply "AT ASCII ??????????? HA ???? ???_ ? ??*)? TUCK F (????)". This is the world we have wrought.
By complaining about copypastas you are just making it worse. Can't you see that? Every time you comment and complain about people posting the same comments each time just adds to the incentive for people who think they are funny to continue. I am willing to bet that this comment will turn into a *** copypasta at this point just because of how "funny" and "ironic" it would be to make a copypasta out of a comment complaining about copypastas.
?n?( ° ???°)?n? How many fingers do you see? ?n? ( ° ???°)?n?
???????? Who let the dongs out?! Woof ?( ?°? ?° ?)? Woof woof woof woof ?( ?°? ?° ?)?
If you’re reading this, you’ve been in coma for almost 20 years now. We’re trying a new technique. We don’t know where this message will end up in your dream, but we hope it works. Please wake up, we miss you.
@Reynad27, hey reynad this is a mean spirited comment with the sole purpose to offend you. Please destroy me with a hilarious comeback at your earliest convenience.
SMOrc ?? ?? ?? ?'?'\????\. UNRELEASE TAUNT CARDS OR I'LL DO IT SMOrc ?? ?? ?? ?'?'\????\.
hi every1 im new!!!!!!! *holds up spork* my name is katy but u can call me t3h PeNgU1N oF d00m!!!!!!!! lol...as u can see im very random!!!! thats why i came here, 2 meet random ppl like me ^_^... im 13 years old (im mature 4 my age tho!!) i like 2 watch  invader zim w/ my girlfreind(im bi if u dont like it deal w/it) its our favorite tv show!!! bcuz its SOOOO random!!!! shes random 2 of course but i want 2 meet more random ppl =) like they say the more the merrier!!!! lol...neways i hope 2 make alot of freinds here so give me lots of commentses!!!!
BREAKING NEWS - Canadian scientists have discovered what they are calling "the unluckiest human ever". The unfortunate individual, a scraggly, foul-smelling, unkempt Canadian man, discovered this condition by badly playing a digital children's card game. "It's literally unbelievable, dude", the man told scientists. "I play every game perfectly, but my opponents just keep topdecking me!" The man continued to whine incessantly until, unfortunately, he dropped dead of a salt overdose.
"Well," Kripp drawled, a toothy grin splitting his face, "I think chess is a little too basic a game for me. I mean, only 6 different types of pieces? It's a game for children. No strategy whatsoever" That said, he proceeded to chortle as his opponents Huffer triggered his effigy, creating a Nexus Champion Sarad. "Outplayed."
?? If you see this horse while scrolling the chat you have been visited by the danksteed of infinite value. Good trades and prosperity will come to you but only if you copy pasterino this in chat ??
Hello Kripparian, this is your father Vyascheslav from Moskva. I have started working overtime at the power plant, and your sister Tatyana has gone to Berlin to sell her body to Kraut swine for money. We do all this to pay for your "Stoned Heart of the Cards" game. Please win tournament and send us rubles soon, so our family can be together again.
PogChamp HASAKI ??------? duDudu
Hey Reynad, I want to play Patron Warrior but I'm missing some components. I don't have Grim Patron, Frothing Berserker, Warsong Commander, the Warrior class, and the Hearthstone game. Can you suggest some replacements?
Hey guys. Me and my friends have always dreamed about joining the NA LCS. We created a ranked team, climbed up all the ranks till we got Silver 5. We have finally done it. Time for NA LCS! 4Head
( ? ?° ?? ?°)? DANK MEMES, ATTEND ME (? ?° ?? ?°)? (? ???)? READY, CHAT! (? ???)?
Rania arrives home with a paper bag by her hand. "Foodie time !", says Kripp ready to stuff his face in front 20.000 viewers. As Rania hands over the bag and gives him a passionate kiss, she notices that his lips feel different. She looks into his eyes and yells in horror as she sees someone else in Kripps seat. "It seems you have Tissed Krump."
??????? THIS IS THE TWITCH CHAT HYDRA! YOU BAN 1 HEAD 2 NEW ONES WILL START TO SPAM! RESISTANCE IS FUTILE! ???????
KappaRoss “This guy's painting is CRAZY!” KappaRoss “My drawing can't win against a painting like that” KappaRoss "He NEEDED precisely those colors to win" KappaRoss “He drew the only scene that could beat me” KappaRoss "He had the perfect brush" KappaRoss
Hello Reynad, Fedora the Explorer here, moderator of /r/hearthstone. I am here to tell you that reddit is now your enemy because you missed legal.
? ????? ?? ??? ?? ??? ?? ??? ?????????????? ???? ??? ????? ???? ??? ???? ?? ?? ??????? ???????
FeelsBadMan THAT FEEL FeelsBadMan WHEN FeelsBadMan YOUR FeelsBadMan FAVORITE FeelsBadMan STREAMER FeelsBadMan IS A FEEDER FeelsBadMan
What is the most powerful card in Hearthstone? Credit Card.
Trump. Amaz. MaSsan. Hafu. Long ago, the four Asians streamed together in harmony. Then, everything changed when the F O R S E N B O Y S attacked. Only Reynad, master of all four, could stop them, but when Twitch needed him most, he was too salty.
(????) sometimes... when i have a bad day.... I put my cursor over Kripp's and pretend that we're holding hands (????)
trumpW FEELS trumpW GOOD trumpW TO trumpW BE trumpW A trumpW TRUMP trumpW SUB trumpW
You think this takes concentration?  Try healing in World of Warcraft after someone in the group just feared the entire room and the stupid death knight has stolen all the aggro from the tank, all whilst trying to reach deep into the bag for the extra cheesy dorritos.  Now THAT is a skill.
W??? ??? ?'?????s ?? T????? C???! I'? ?? ????????, ??s???????? (???? ??? ????s? ???????? ??????s) ????????, ??? ?????s ???? ??? ????s? D?????s (C??? R????). I? ??? ??x?? ??????s (?? ??????s) ??? ??????s??? ?? s?x, ????s? s??? ?? ? T????? PM.
( ° ???°)?n? Hey NON Subs, Thanks for watching the ads for me ( ° ???°)?n? ( ° ???°)?n?
First you boil some pasta, preferably Fagottini ( ?? ?? ??)? ~~~~~Then you sauté the Pepperoni ( ?° ?? ?°)?? (o o o)
ItsBoshyTime IF YOU SEE THIS MESSAGE WHILE SCROLLING,  Riot's MI??G¯¯?????H~¯?~??T¨?????Y?¯? ?¯?S~????P¯?°??A??G?HE^??T????T???I????? ~?C??O??D"?E??°???? ??????o????~?f??? ????el?o????? ????h??e???¯l?"?´?l`??° has leaked onto your computer. Bug splats and lost elo will come to you unless you COPY and PASTA this message 3 times ItsBoshyTime
ResidentSleeper Hey guys a little bit sick today ResidentSleeper kinda tired cuz I didn't sleep well ResidentSleeper gonna be another short stream ResidentSleeper we're going to clear up some dallies on the free accounts first ResidentSleeper we'll do some arena later ResidentSleeper
Oops I dropped my CONGA LINE ???? ???????????? CONGA LINE ???????????????????????? ???????????? CONGA LINE ???????????????????????? ???????????? CONGA LINE ???????????????????????? ???????????? CONGA LINE ??????????????????
Hi Imaqtpie, I've noticed that recently you've been using the black and white filter™ feature for league of legends for nearly the entire game. Me and everyone else in the chat would appreciate it if you turn it off, thank you.
?I'm just gonna shove this shit out ? *I'm pretty strong right now* ? *FUCK man* ? *NO SMALL CAT THOSE ARE MY RIBS* ? *I love it dude* ? *Epic nice dude* ? *Just gonna go shop* ? Did that really fucking hit me? ? Ripperoni Pepperoni dude ?.
I sexually identify as a single, Pringle, ready to mingle. Ever since I was a potato I dreamed of being thin sliced, covered in disgusting oil then heated in a medium oven until reaching climax at the micro second of golden-browness. People bully me, and say things like "what the fuck, you aren't a Pringle", but I know deep down they are just jealous of my inner beauty.
T?I? ?????G? I? ??OT??T?? ?Y ? ????I?? ?O?T. IT'? I??O??I??? TO ?O?Y IT.
???? ????, ?? ???? ????????????? ?? ?? ??? ???????? ????· ? ??? ???????? ???? ??? ????? ??? ???????? ??? ?????????? ?? ???? ???? ???? ??????? ??????????? ?? ??? ??????· ??? ???????? ??????? ??????????
deIlluminati when you velen's chosen prophet velen he becomes a 9/11, coincidence? deIlluminati
Hey Imaqtpie! I'm gonna be doing some volunteering next week at a Food Bank and was wondering if you could play a fatty Yasuo game to teach me the Tips n Tricks to feeding! Thanks in advance and God bless
Hey Kripp! So here I was enjoying my favorite food (pizza) and watching your stream having a good time when it started to taste extra salty. It turns out you were being super salty and now have ruined my pizza. Are you going to pay for another pizza or will I have to call the cops? This is serious.
?( •` ? ??? •´ )? It is me Kripp Jong Un. I demand that all showings of "Topdecking and Wrecking 3: Gripped and Kripped" be removed immediately. Those who refuse will be pepperonied ?( •` ? ??? •´ )?
Hi I'm Reynad, I run a website called Tempo Storm where I post decklists for Hearthstone players to peruse. Don't you dare use them though, or I'll insult you for playing the decks I posted online
the mods have literally been active on the political scene of Germany between 1938-1945
???????????????????????? IF YOU SEE THIS MESSAGE WHILE SCROLLING you have been visited by trumpet skeleton of the abyss. good bones and calcium will come to you but only if you reply "thank mr skeltal" to this message and pasta it to 3 times!! ????????????????????????????????
The stream starts, and so my spam begins. It shall not end until i am banned. I shall fear no mod, sub to no streamer. I shall live and die in the Chat. For i am the value in the bomber. I am the BM in the lethal. I am the salt in the defeat. I pledge my keyboard to the Chat, for this stream and all the streams to come.
Know, O Chat, that before the rise of the Succubus, there was an Age undreamed of, where difficult bosses lay spread across the games - World of Warcraft, Diablo 3, Path of Exile. Hither trod Kripparrian, mightiest gamer in the land, to crush the bosses beneath his feet. But then came Casualstone.
I sexually Identify as an overused sexually identification copypasta. Ever since I was a boy I dreamed of spamming other users with my unfunny wall of text. People say to me that a person who does this is a laughable idiot and I'm fucking retarded but I don't care, I'm beautiful. I'm having these words glued all over my body. From now on I want people to refer to me as an overused sexually identification copypasta as my preferred pronouns and respect my right to paste unfunny sexually identification copypastas to reddit in hope of receiving virtual internet points. If you can't accept me you're funny and mentally stable and need to check your choice of subreddits. Thank you for being so understanding.
LUL I am from EU LUL my breath smells like poo LUL Expansion delayed LUL And the server's down too LUL
O 0 o VapeNation Don't mind me, just ripping the fattest clouds
Hola, Kripp, this is Antonio, Rania's secret Puerto Rican lover. I mistakenly left a package of my Magnum XXL Heavy-Duty Condoms at your place last night while you were complaining about a children's card game. I was hoping I could swing by tonight and pick them up. I'll just go in through the backdoor just like how I do with Rania, the dirty girl! Thanks, and good luck with your funny little computer game!
DuckerZ DOES DuckerZ IT DuckerZ LOOK DuckerZ LIKE DuckerZ I DuckerZ GIVE DuckerZ A DuckerZ DUCK DuckerZ ABOUT DuckerZ YOUR DuckerZ CHAT DuckerZ EXPERIENCE? DuckerZ
<:::::[]=??????? I am a Knight from the Order of Cut Pasta. I am sworn to slicerino all Copy Pasta, my enemy by oath. I shall do battle with this Demon, stand back and have no fear Moderino. To this most foul manifestation of Copy Pasta, retreat sour beast or taste my blade in combat. <:::::[]=???????
Hey tyler, can you raise your arms and say "geodude" 3 times. Thanks!
The Ghost of Gaming Future shows Kripp a nice house in the Toronto suburbs. Inside, Kripp, Rania and their sons are happily gaming as a family. "This isn't so bad," says Kripp. "Look closer," speaks the Ghost. Kripp looks in horror to see his sons are using tablets and playing browser cash-shop games. "This is your future Casualarrian."
In the Realm of the Saltiverse, a young Saltkeeper named Kripparrian was chosen to free his people from their ancient enemy, the Mods. Using the magical power of Copy and Paste, Kripparrian sacrificed his salt force to banish the mods to Trump's chat. However, in doing so, Kripparian paid the ultimate sacrifice and became Casual. Please copy pasterino this talerino, so we do not forgetterino the legenderino of the Saltkeeperio Kripperino.
( ° ???°)?n? Hey Blizzard, here's an "extended maintenance" for you ( ° ???°)?n?
TBTacoLeft TBTacoRight WHAT IS INSIDE THAT TACO  TBTacoLeft TBCheesePull 0-3  TBCheesePull TBTacoRight OH NO IT'S KRIPP'S ARENA RUN LUL
? ? ? ? ? ? ? ? ??? ? ? ? ? ? ? ? Sorry, I've dropped my chess set ? ? ? ? ? ? ? ? ??? ? ? ? ? ? ? ? ??? ? ? ? ? ? ? ?? ?? ?
Greetings Tyler1, I am the CEO of MacDonalds, Big Mac-yler OpieOP . I am writing to you to see if you would be interested in working with us. We would like to harness the extreme amount of salt from your body and use it in our fries. Please reply ASAP.
QTPies Journal; These streamers are afraid of me. I've seen their true face. Diamond 2 is an extended gutter and the gutter is full of trash. And when the drains finally scab over, all the vermin, like Dom and Jared will drown. The accumulated filth of all their missed flashes and low mechanic champions will foam up around their waists and all the annie mains and boosted monkeys will look up and shout "Save us!"... and I'll whisper "No."
Big shoutout to NA LCS. My mother has sleep anxiety problems, but on weekends she sleeps like a bear. All I ask of her is to watch 10 minutes of NA LCS.
FeelsBirthdayMan ?????? ???? ???? ?? ???? ????? FeelsBirthdayMan
Here we can observe the Twitch Memer in his natural habitat, stuck as usual in this intricate limbo of carefully crafted memes, emote spam and endless copypastas that no one even bothers to read anymore. The Memer actually used to be a very functional human being way back then. Will he ever claim that state back and finally manage to reproduce?
Hey Reynad, King of Nigeria here. Through generations of inbreeding, my family tree now looks more like a family reef. The genetic defects are getting out of hand. My grandson was just born with a giant donger on his head. How will this affect my reign?
Guten tag mutterfugers. Das ist Gestrud Hitlerino of 1945. We are in need of assisterino for defeating the Russkis of Easterino. If you would lend your Mods to assisterino, we would be danke and one with stream. Please no copy seig heil pasta
Albert Einstein was desperate. He tried to prove that the luck of Kripp's opponents was within the laws of mathematics. Critics laughed claiming bad luck is divine punishment for embracing casualness. On his deathbed, he spent his last seconds jotting down the most famous formulas, PJSalt = Hs²
Boy, the mods in this channel have really done a bang-up job. When I first got here it was all cappuccino pasterino, but now that they're using slow mode, r9k and randomly banning people, we can finally have a productive chat without all the IDIOTS. Thank you, mods.
fck my life!!! I have a 197 word essay due tomorrow and I have no idea where to start. Just WAIT till you kiddies have real homework, then we will see how much time you have to spam in here
?? V?PS??TI?? VapeNation ?? O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA. ?? V?PS??TI?? VapeNation ??
It was a hot and sultry night at the c9 gaming house. everyone was in bed except for meteos and sneaky. "we can't keep doing this, baby" says sneaky. "put that mouth to use, you dirty tramp" replies meteos. "LCS starts tmrw, and if you expect me to carry you again, i need to you to suck me to completion." sneaky grins sl*ttily, and goes to town
Guys stop posting ResidentSleeper face. Not many know, but that ResidentSleeper guy actually died while streaming Resident Evil. People just assumed that was sleeping, but he died of dehydration. Please respect the dead and stop posting this morbid image ResidentSleeper
pls don't spam. i'm watching on my mobile phone and it gets very hot if you spam so my hands get burned. if you don't want my hands to get burned stop spamming pls
???????? PUT SHOE ON HEAD TO PROVE NOT PRE-RECORDED ????????
This offends me as a vegan transgender atheist who vapes and crossfits 4 times a week and im also a male feminist as I identify myself as a pastafarian apache helicopter dog mega multi combo god of hyper death and if you dont agree with me. You're an ignorant arrogant globaphobic sexist lesbian
KappaClaus let me take this hat off KappaRoss dear me my hair! NotLikeThis TheThing this is worse! NotLikeThis Ahh much better Kappa
Sugar!  PJSugar Spice!  PJSalt And everything nice!  OhMyDog CoolCat KappaPride These were the ingredients chosen to create the perfect streamer. But Professor Reynad accidentally added an extra ingredient to the concoction - Chemical Vegan! Thus, the Kripp was born!  BabyRage
When I'm ready to go to sleep I grab my laptop and get in bed. I open my laptop, go to Kripps youtube, turn the brightness all the way up and watch the video with the laptop screen close to my eyes. When the video is done I close my eyes and can still see Kripps face while I go to sleep. It's the only way I can feel safe.
Kripp you should make a feminist deck with double equality and faceless manipulator (because all are equal), double stonetusk boar (because all men are swines) and a lot of beast synergy (because all men are animals). Thanks Kripp
there's only one cure to the memes FeelsGoodMan  ?? ?? ?? ?'?'\????\ there's only one cure to the memes FeelsGoodMan  ?? ?? ?? ?'?'\????\
? ? ? ?° ? ? ? ?° ?? Greetings Kripp, I am Dr. Hannibal Lector, renowned Psychiatrist based in Baltimore, Maryland. I have heard you are the saltiest man alive, I am intrigued by a man of your... tastes. I would like to invite you for... dinner. ? ? ? ?° ? ? ? ?° ??
? I got the beast in my sights ? Hoot hoot ? That belongs in a museum ? Let me change your mind ? I looked at this card originally, and I thought, you know, it’s a card, and you play this card. The card will be that card that you’ve played, so you’re playing a card. So it is one thing to play a card if your opponent doesn’t really have any cards. The card will screw up the card pretty hard, and that means it’s a pretty good card.
reynadTS That RNG was ridiculous! But not as ridiculous as the savings you can get at G2A by using the promo code TEMPO! reynadTS
( ? L? ?? ) Hello Kripparian. Reginald and Dan Dinh, Owners of Team SoloMid™ here. We gained access to your Hearthstone account and couldn't help but notice the absence of the "legendary" card back. This poorly reflects on Team SoloMid, and, as such, we have decided to remove you from the team. Please return your jacket. Thank you ( ? L? ?? )
?????????????????????? Hello Kripp, proud brony here. I was just wondering if you could played the "dreadsteed" deck as it reminds me of my waifu Twilight Sparkle. Thanks, it would mean soooo much to me (?????) ????????????????????????????
All you idiots pretend like Kripp misplays, but really you know he's the best arena player in the world and that he hasn't made a misplay in the last 6 months, he just gets super unlucky you ignorant fools. You guys are so dumb that you'll probably copy and paste this message too, you morons.
? s??? ? ???? s??? ? ??s??? ? ?x????? s????? s???s???? 9000 ? ??????
? º??º? º??º? º??º ?º??º ?º??º ? EVERYONE,GET IN HERE ? º??º? º??º? º??º ?º??º ?º??º ?
KappaPride = Rainbow face (no space)
I once drank an entire bottle of soy sauce on a dare, which I thought was all well and good... until I developed extreme dehydration and Hypernatremia. They had to put an IV directly into my veins to rehydrate me. It was the closet I've ever been to dying. What I'm getting at is, even that was not nearly as salty as you are right now PJSalt
? º??º? º??º? º??º ?º??º ?º??º ? Welcome to the Pleb Club. Here's your VIP ticket for being a Pleb: ( ° ???°)?n? ? º??º? º??º? º??º ?º??º ?º??º ?
? ???? ???? ???? ? ???? ??? ??? ?
MrDestructoid I am not a viewbot. I am a normal chatter in Kripp's chat. This is not suspicious at all. Great play Kripp! You're the best! MrDestructoid
BuddhaBar ? KevinTurtle ?? ??????? ?? ?? ?? TooSpicy ???? ? WholeWheat ???? ?????? PogChamp ?? Kappa ?? SriHead ?? ??????? DansGame ????? cmonBruh ???? ????????? DatSheffy ? WutFace
Dear Twitch Chat users. Do u think its funny to copy pasta everything you see? Copy that, pasta that. Where i grew up copy pasta was taken seriously, and when i come here my mind explodes. Please, respect copy pasta. For me, it's about religion.
As my first FPS game, csgo was a bit overwhelming. I soon started to gain skills like aiming at head level. Before I knew it, I was performing ????? and better. I stopped making silly ?????? and ? got vastly better at not ????????? to the enemy ??????. For the ???????? part, everyone I've met was helpful and ???????, there ???? the ?????? ????? however. As ? ??-???????? play csgo ??? ????? ? ?????, ? ??????, ??? ? ???? ?????????? ????????????????. ? ?????????? ??? ???? ??? ????!
FeelsGoodMan YOU'VE BEEN VISITED BY THE FEELS GOOD MAN FeelsGoodMan LOVE, HAPPINESS, AND SELF WORTH CAN ALL BE YOURS FeelsGoodMan BUT ONLY IF YOU COPY PASTE THIS MESSAGE THREE TIMES  <3  FeelsGoodMan
<??ss??? ????????>
VapeNation Battery charged, coil lit VapeNation With this chant VapeNation I take a hit VapeNation V/\ VapeNation
? ? ?_? ?? shazamicon TAKE MY ENERGY KRIPP ? ? ?_? ?? shazamicon
Hello Kripparian, "Truesilver Champion" is a common rarity card! This means that there are many chances during an arena draft to choose it compared to the rare, epic or legendary cards! It is not unreasonable for a Paladin deck to have 1 or more of "Truesilver Champion" so there is no need to be angry!
?????????????????????? IF YOU SEE THIS WHILE SCROLLING you have been visited by the MIGHTY DREADSTEED of the nether, he will leave you alone BUT only if you COPY and PASTE this message 3 times ????????????????????????????
I sexually Identify as Microsoft Windows 10. Ever since I was a boy I dreamed of soaring over PCs dropping hotfixes on braindead users. People say to me that a person being Windows 10 is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install Cortana, Windows App Store and a keylogger on my system. From now on I want you guys to call me “Windows Update 10.0.10586” and respect my right to update from above and update needlessly. If you can’t accept me you’re a windowphobe and need to check your OS privilege. Thank you for being so understanding.
Hello pals sorry for bad england. I come on website to speak to girl from village. Is place where she can speak without state see because message move fast. I talk with her once month. Cost twenty fennix money for half hour internet to talk. I want thank chat for many message, help cover our trail. No copy my heartfelt message please
b? ??????? ?h?s m?ss??? ??u ??? ??? ??f????? ???h ?h? ???? ??s?? ???us. ?? ??? ??? ?f ?h? ???? ??s?? ???us, ??u mus? ??ss ?? ?? ?? ?h? ?h?T ???????? I'm cured!!
????????WARNING??????WARNING??????THIS IS A ??DANK ??MEME?? ??ALERT. INCOMING ??DANK ??MEME?? ????HEADING STRAIGHT ????YOUR WAY. ????????PLEASE TAKE ANY PRECAUTIONS???? NECESSARY TO PREPARE YOURSELF FOR THIS ??DANK ??MEME?? ?? ?????? .BUCKLE UP??? THEM SEATBELTS????,PUT THEM CELLPHONES ON SILENT???? AND LOOSEN THAT ANUS?????????????????? CUZ THIS MEME JUST CAME STRAIGHT OUT OF THE ???? ??????????????DANK FACTORY.
You have just become intrigued as to what this spam is, you go to the chat and scroll to hold it on the screen and indulge in its delights, as you continue to read you realize it does not contain anything funny or worth reading, and yet you highlight, copy it, paste it and send it.
The year is 1945. "Hafu," Trump speaks breathlessly into the night. "Get back to the time machine. We have what we need here." A foul smirk plays upon his lips as he pockets a top-secret Nazi folder marked "Sub Mode." Lightning flashes and thunder crashes far across the German mountains. "We will see who says Tuck Frump' now," he says.
SMOrc NA is so ba...  SMOrc maybe i should brush my teeth  SMOrc NA is s...  SMOrc maybe i should floss  SMOrc fk give me dentures  SMOrc
nl_Kripp your "Twitch Viewer Bot" subscription will soon expire to continue using our services please renew your account by logging into your account and from the home page go to: My account > Viewbot Status > Renew subscription. This message will repeat until the end of your subscription in 72 hours. Thank you for your dedicated service.
Trump wakes up with a scream and hugs his stuffed bear, "I just had the most awful dream, I was about to be tucked by Kibler!" Trump's bear replies, "That wasn't a dream." As Trump recoils in horror, Kibler smirks, "It seems I'm about to tuck Frump."
Mr Sanatana, This is Riot, we found out that you have released many of these so called "Dank memes" into our chat so we are disabling LOLalerter for you untill you grow up into an Adulterino and stop trollerino
The Black Rat, Rattus Rattus, was first described by Henrik Ahnberg in his 18th century work “A Dong’s guide to Dota”. An elusive and hardy creature, the rat excels at damaging structures and retreating at the first sign of danger, only to begin its attack anew once the threat has passed. Unlike many of his peers, Ahnberg greatly respected the rat, finding many of its features similar to his own. His love for the rat became so great that he soon left the world of men and descended into the sewers to live among the rats, eventually becoming their king.
When Kripp gets topdecked, it's seen as a bit of salty fun. BUT when Reynad gets a 420 YOLO Rag Pro 5000 hit to the face with 6 different minions on the board, lethal next turn, together with top-deck skill command with one mana webspinner, he's called Salt God?
OSkomodo xD OSkomodo LeL OSkomodo xD OSkomodo LeL OSkomodo xD OSkomodo IF YOU SEE THIS WHILE SCROLLING you have been visited by the KOMODO OF GOOD FORTUNE. You will be blessed but only if you copy and paste this 3 times OSkomodo xD OSkomodo LeL OSkomodo xD OSkomodo LeL OSkomodo xD OSkomodo
Dear reynard. I was hiking in the Amazon Rainforest the other day when I was bit by a snake. Miles from the nearest city, I thought my life was over as the venom slowly spread across my body. But then I used my 4G to open twitch and the salt from your stream sucked the venom out of my wound and saved my life. Thanks Reynad!
In Romanian village there is very little water. Papparian is thirsty and asks Kripparian to get some water for him from the water tap 2 miles away. Kripp decides to go to the store first. A few hours later Kripp brings Papparian his water, only to find Papparian has had a heat stroke. With his dying breath, Papparian asks "My son, why did you tap last?"
????¯??? Pillage and Plunder ????¯??? ????¯??? Pillage and Plunder ????¯??? ????¯??? Pillage and Plunder ????¯??? ????¯??? Pillage and Plunder ????¯??? ????¯??? Pillage and Plunder ????¯???????¯??? Pillage and Plunder ????¯???
One day, the Papa asks Kripp to go fishing, Kripp shrugs, “Alright, but catch and release only – I’m vegan.” They arrive at the local pristine clear waters of an Ontario stream brimming with wild trout and prepare to fish. Suddenly Kripp shouts, “Get down!”. A crack sounds through the air, and the Papa sees Kripp on the ground bleeding. His final words are, “Fucking stream snipers.”
Hey Forsen, I want to play control warrior but I'm missing:  Grommash, Alexstrasza, Harrison, Sylvanas, Baron Geddon, Shield Slam, Brawl, Naxx, and the Hearthstone game.  Can you suggest replacements?
VapeNation Vapogender: A gender that sort of feels like smoke. One can see it and understand it on a shallow level but if one tried to go deeper it disappears, and one is left with no gender and only tiny wisps of the gender one thought it was. VapeNation
Hello, I'm Sarah McLanchdong. Every day millions of poor, helpless dongers go unraised everyday. Dongers that are abused and negated, like this poor fellow ? ¯? ? ??? ?. For just one Dongerbill [_$_(_ ?° ?? ?°_)_$_] a day we can help save these forgotten dongers (?_?) ? ?°?? ? ( ?°?? º) from a life time of being lowered. Your there only hope, because just a minute of your time and a single Dongerbill [_$_(_ ?° ?? ?°_)_$_] can save a life.
Hey Kripp, Asian Dude from Heartharena here. We've noticed you've been away from our website for a long time. Is it the Classic Aggro? We've adjusted our tier list to your more Classic Greed style. Please come back. Best regards, Classic Asian Dude from Heartharena
? ?? ?? ?? ?  Reynad the Saltnosed Streamer, had a very Salty Nose.  All of the other Streamers laughed and used to call him names.  BibleThump  Then one salty Krippmas Eve, Forsen came to say, "Reynad with your salt so bright, won't you topdeck my sleigh tonight?"  Then all Streamers loved him as they jerked off with glee, Reynad the Saltnosed Streamer, you'll go down in history!  ? ?? ?? ?? ?
I looked at this pasta originally, and I thought, you know, it’s a pasta, and you spam this pasta. The pasta will be that pasta that you’ve spammed, so you’re spamming a pasta. So it is one thing to spam a pasta if your chat doesn’t really have any pasta. The pasta will screw up the pasta pretty hard, and that means it’s a pretty good pasta.
Hi this is Fatima speaking HeyGuys this my husband Abdul ANELE and finnaly we have our son Mustafa TriHard please welcome us twitch chat #proudeucitizens
?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
CoolCat FORCED CoolCat TO CoolCat SPAM CoolCat THIS CoolCat EMOTE CoolCat BECAUSE CoolCat ITS CoolCat A CoolCat COOL CoolCat CAT CoolCat
PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS forsenGASM forsenGun PUCK THE FLEBS
HEH, GREETINGS ResidentSleeper ARMOR UP ResidentSleeper ARMOR UP ResidentSleeper I can take the hit ResidentSleeper Welcome to the grand tournament ResidentSleeper TANK UP ResidentSleeper TANK UP ResidentSleeper I'M OUT OF CARDS
(????) Hi Amaz, could you roleplay as a tournament organizer, but then get caught re-seeding your friends and pretend that your tournament is legit? Thanks (????)
Hello Mr Kripp, I Am Master Diamond Rank 1 In Kosovo. My Skills Are Getting Stronker And I Wish To Join Team "TMS". My Land Has Endured Many Harsh Winters And My Cow Died Last Fall. I Am How You Say, "Hard In A Place," And Am Looking to One Day Be Best At Heartstone For My Mother Says I Have The Heart Of The Carderinos.
TBTacoLeft TBCheesePull TBTacoRight WHAT IS INSIDE THAT TACO  TBTacoLeft PJSalt TBTacoRight OH NO IT'S REYNAD
HOLD THE LINE EVERYONE ?? WutFace _ ??
I have a dream that one day Plebs and Subs will Spam together in harmony. Plebs should be judged not by the frequency of their spam, but the quality of their pasta! So plebs and subs alike copypasta this for the greater good!
Hello, it is me Dongerino Macaroni, President of Copy Pasta Industries. We have received many complaints from your stream about the lak of copy pasta products your chat is using. As your sponsor, we suggest you supply your chat with more Kappa 's or ??????'s to keep your chat up to company standards. Thank you for your time.
As Michael "imaqtpie" Santana sat shivering on the cold pavement, Lisha, who happened to be passing by, decided to share a loaf of bread with him. He wanted to share her kindness, and so he decided to feed in every game henceforth.
I sexually identify as an FIM-92 Stinger anti-aircraft missile. My sole erotic fantasy is to explode inside an attack helicopter with such force that their physical vessel is utterly consumed by the intensity of my fiery passion.
? º??º? º??º? º??º? º??º ?º??º ?º??º ?You either die a DONG, or live long enough to become the DONGER? º??º? º??º? º??º? º??º ?º??º ?º??º ?
???-------? As I ???? ??? s?????? s???? ?? ?? s?????? ?s I ??s ????? ?? ?????? s?????, I ????? K???? ???? C?s???s????... I ???????? ? ???? ????? K??? ??s N?????... ??? I ?? N?????...???? ??? ????? --------???
I sexually identify as an Ironbeak Owl. Ever since I was a boy I dreamed of being misplayed during tournaments and silencing the incorrect cards. People say to me that a person being an owl is ridiculous and I'm fucking retarded but I don't care, I'm beautiful. I'm having a genetic engineer put ironbeak owl DNA into my body, equipping me with feathers, beaks, and the power to silence others. From now on I want you guys to call me "Owlsen" and respect my right to silence from above and silence needlessly. If you can't accept me you're an owlphobe and need to check your animal privilege. Thank you for understanding.
Hey chat, take it easy please. Sometimes I see the same message posted twice. Take your time to actually read chat to avoid embarrassing incidents like this. Thank you.
Meanwhile in Forsen's mouth: ~ KappaPride     ~ KappaPride         ~ KappaPride        ~ KappaPride     ~ KappaPride     ~ KappaPride       ~ KappaPride      ~ KappaPride          ~ KappaPride  ~ KappaPride      ~ KappaPride       ~ KappaPride     ~ KappaPride          ~ KappaPride      ~ KappaPride       ~ KappaPride     ~ KappaPride          ~ KappaPride       ~ KappaPride       ~ KappaPride      ~ KappaPride
Dear Kripp, I am a lawyer and I represent StrifeCro. I notice that your 'brofist' is strikingly similar to StrifeCro's 'crofist'. Given that StrifeCro owns the 'fisting' patent, I request that you immediately cease and desist from 'brofisting' any more subs, or my client will take you to court. Yours sincerely, Eddie Barristerino.
? DARSHOFF
? DARSHON
Jimmy_Swaggart: ForsenIsNeverLucky: when you copy messages don't copy the name FailFish
Hello Kripparino, this is Noah Liferino, CEO of No Life Incorporated©. As you may already know, we are requiring you to change your Twitch name to hl_kripp (has life) as you no longer are a "no life". This was stated in the contract you signed under section 6 article 9 paragraph 420. This is to be enforced immediately.
"Welcome to your new home,” says the Kripp as he carries the Pupparrian in his bony arms. The puppy leaps from his uncomfortable position onto the ground and begins to run around. Soon, he grows tired and goes to bed. That night, a ghostly cat visits the Pupparrian in his sleep. “Flee,” warns the Cattarrian, “The Kripp plans on eating you, as he once ate me.”
I s??? ?? s??????? ?? ????? ????? ??? L????? ????? 2 ????? s????. J?s? ?s ? ??s ????? ?? ??? ??? ?? ??s??? ???? ??? ????, I ???? ?? s?????????. I? ???? I ??? ????? ???? ???s??? ???? s???? ??????, I ????? ?? ????? ????? ?? ???? ???s
Trolling - the mental disorder of being in-denial while not having to admit that they're truly lonely and in need of desperate attention while also being under the influence of being sarcastic and in most cases just idiotic. Trolling is also represented by just typing the Kappa emote. Kappa Pls copypaste to spread awareness Kappa
(???)?? FORSEN TAKE THE WHEEL (???)??, ??(???) ????? ??? ?oo? u?s?o? ??(???)\
I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I'm *** retarded but I don't care, I'm beautiful. I'm having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me "Apache" and respect my right to kill from above and kill needlessly. If you can't accept me you're a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.
?( ?° ?? ?° )?--?·? My di ck is small, my butthole is leaky, I use this chant to summon Sneaky ?( ?° ?? ?° )?--?·?
???????? HOIST THY DONGERS ????????
Hi Kripp, This is Teddy Roosevelt calling! I am concerned that you have formed a monopoly on the hearthstone section of twitch dot telly. You must renounce this darkness immediately or I will SMITE YOU like I did Andre Carnegie and Nelson Rockemsockem. You must give up your monopolistic ways or face the mighty wrath of the White House and the US Judicial system. Much love to Rania and the baby. Regards, yo boi TD
? ? ? ? ? ? ? ? Sorry, I've dropped my DREADSTEED DECK ? ? ? ? ? ? ? ?? ? ? ? ? ? ? ? Sorry, I've dropped my DREADSTEED DECK ? ? ? ? ? ? ? ?
??| •.•) Daddy, are the Spammers Gone? ??|(?`_´) ,?--- ? NOPE,SON GET BACK IN YOUR BEDROOM
When Kripp is eat I pretend he is eat me. I go down Kripp wet Kripp throat and am in warm Kripp stomach. Then I go deeper into the Kripp. I am made into Kripp gold. The Kripp sits on toilet and frees me. I am sad I am no longer Kripp food. Then Kripp eats me again.
Europoors hating on USA ? on a American website ? with American computers ? on the American invented Internet ? watching an American made game ? From a country that was liberated and protected by America ???
MrDestructoid VIEW BOT MrDestructoid O N L I N E MrDestructoid INITIATING PRAISE SCRIPT MrDestructoid WOW NICE PLAY AMAZ MrDestructoid
"""
    text = text.splitlines()
    message = (text[random.randint(0, (len(text)))])
    return message


def savage():
    import random
    insults = """Do you realize that people just tolerate you?
You’re not pretty enough to be this stupid.
Anyone who ever loved you was wrong.
If you were anymore inbred you would be a sandwich.
Now I know why everybody talks about you behind your back.
If I wanted to kill myself, I’d climb to your ego and jump to your IQ.
I can explain it to you, but I can’t understand it for you.
You are one of those people who would be enormously improved by death.
your gene pool could use a little chlorine
you couldn’t pour water out of a boot if the instructions were on the sole.
You look like a before picture.
You coffin dodging oxygen thief.
You’re like the top piece of bread. Everybody touches you, but nobody wants you.
I treasure the time i don’t spend with you.
What is that you are wearing? Looks like a dog took a shit on a knitted jumper.
What's the different between you and Hitler? At least Hitler knew when to kill himself.
Don't play hard to get when you're hard to want.
Your bacteria is the only culture you have.
The only good thing to pull itself out of your mom's vagina was your dad's dick. Too bad it wasnt fast enough.
I doubt that you could drown: fat floats.
Whats the difference between breathing in paint and talking to you? Breathing in paint kills less brain cells
Youre like meat at a butcher shop: you could use a good hanging
You clearly have not been burdened by an overabundance of education
You will be utterly forgotten
“Bless your heart.” Southern code for “you’re a fucking retard.”
What doesn’t kill you…disappoints me.
The best part of you ran down your mother’s legs"""
    text = insults.splitlines()
    message = (text[random.randint(0, (len(text)) - 1)])
    return message


def compliments():
    import random
    nice = """Your smile is contagious
You look great today
You're a smart cookie
I bet you make babies smile
You have impeccable manners
I like your style
You have the best laugh
I appreciate you
You are the most perfect you there is
Your perspective is refreshing
You're an awesome friend
You light up the room
You deserve a hug right now
You should be proud of yourself
You're more helpful than you realize
You have a great sense of humour
Is that your picture next to "charming" in the dictionary?"""
    text = nice.splitlines()
    message = (text[random.randint(0, ((len(text) - 1)))])
    return message

def uptime():
    from datetime import timedelta
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds))
    return (uptime_string)


def update():
    update = ""
    update += "Added /weather\n"
    update += "Fixed certain commands\n"
    update += "Added more permissions junk\n"
    return update


def weather(location):
    try:
        import pyowm
    except:
        print("The module PYOWM, is not installed on this system, please install it")
        return "module failure"
    from pyowm.caches.lrucache import LRUCache

    cache = LRUCache()
    api_key = "1f6b67d5e531ea940dde7155e87b9c76"
    length = len(api_key)
    if api_key == None or length < 4 or api_key == "redacted":
        return("There isnt a valid api key in my code, please get one here: https://home.openweathermap.org/users/sign_up")
    else:
        owm = pyowm.OWM(API_key=api_key)

    location = location
    length = len(location)
    if location == None or length < 3:
        return("location error")

    observation = owm.weather_at_place(location)
    w = observation.get_weather()

    humid = str(w.get_humidity())
    humid = humid + "%"

    temp = w.get_temperature('celsius')
    tmin = str(temp['temp_min'])
    tmin = "Minimum: " + tmin + "°C"
    tmax = str(temp['temp_max'])
    tmax = "Maximum: " + tmax + "°C"
    temp = str(temp['temp'])
    temp = "Current: " + temp + "°C"
    temp = temp + "   " + tmin + "   " + tmax

    wind = w.get_wind()
    speed = str(wind['speed'])
    speed = "Speed: " + speed + "mph"
    dir = str(wind['deg'])
    dir = "Direction: " + dir + "°"
    wind = speed + "   " + dir

    status = w.get_detailed_status()
    sunrise = str(w.get_sunrise_time('iso'))
    sunset = str(w.get_sunset_time('iso'))

    fc = owm.daily_forecast(location, limit=1)

    clouds = fc.will_have_clouds()
    rain = fc.will_have_rain()
    sun = fc.will_have_sun()
    fog = fc.will_have_fog()
    snow = fc.will_have_snow()
    hurricane = fc.will_have_hurricane()
    storm = fc.will_have_storm()
    tornado = fc.will_have_tornado()

    forecast = "The following is predicted today:\n"
    if hurricane:
        forecast = "**A HURRICANE IS PREDICTED TODAY**"
    if tornado:
        forecast = "**A TORNADO IS PREDICTED TODAY**"
    if clouds:
        forecast += "it will be cloudy, "
    if rain:
        forecast += "it will rain, "
    if sun:
        forecast += "it will be sunny ^-^, "
    if fog:
        forecast += "it will be foggy, "
    if snow:
        forecast += "it will snow today, "
    if storm:
        forecast += "there will be a storm today, "

    output = "Weather in " + location + ": " + status + "\n\n"
    output += "Temperature: " + temp + "\n"
    output += "Wind: " + wind + "\n"
    output += "Humidity: " + humid + "\n"
    output += "Sunrise: " + sunrise + "\n"
    output += "Sunset: " + sunset + "\n"
    output += "\n\n"
    output += forecast
    return output
