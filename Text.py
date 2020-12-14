# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image r icon1 = 'Rob.png'

image first h = 'first h.png'
image Rob face = 'Rob face.png'
image Map = 'Map.png'
image first h2 = 'first h2.png'

#the park
image two path = 'two path.png'
image small girl = 'small girl.png'
image old lady = 'old lady.png'
image Bad end = 'Bad end.png'
image Bad endp = 'Bad endp.png'
image Bad endm = 'Bad endm.png'

#the city
image the city = 'the city.png'
image bank = 'bank.png'
image homeless = 'Homeless.png'
image bankm = 'bankm.png'
#Characters
define r = Character ('Rob', color='#9161CC')
define x = Character ('???', color='#890000')
define l = Character ('old lady', color='#D14DAD')
define b = Character ('Bank lady', color='#9CDBE2')
define h = Character ('Homeless', color='#B4D893')
# The game starts here.

label start:



    scene first h
    with fade


    show r icon1



    r "Welcome to my garage fellow Robber."

    r "You have to help me with some robbery or I will starve to death."

    r "As you can see I only have a wheel left and 3 coins."

    r "I was forced to sell my precious car to survive."

    r "Anyways where do you want to go fellow robber.?"
    scene Map

    menu:
        "The City":
            jump City
        "The Park":
            jump Park
    label City:
        r "Might be some weird people around here so be careful."
        scene the city
        r " Well there is a homeless and a bank, which one do you want to go for fellow robber?"

        menu:
            "Go for the homeless":
                jump homeless
            "Go inside the bank":
                jump bank
        label bank:
            scene bank
            b "Hello what can I help you with?"
            r "Give me 20000 euro right now or I will shot you!"
            b "Okay, Okay just take it"
            scene bankm
            r "Thank you lady I shall leave now."
            scene Rob face
            r "Mission completed"
            return

        label homeless:
            scene homeless
            h "What are you doing out here boy"
            r "Just walking by."
            h "Do not try anything funny or you will have a bullet through your head."
            r "Relax."
            menu:
                "Go Inside the bank":
                    jump bank2
                "Go to the park":
                    jump park2
            label bank2:
                scene bank
                b "Hello what can I help you with?"
                r "Give me 20000 euro right now or I will shot you!"
                b "Okay, Okay just take it"
                scene bankm
                r "Thank you lady I shall leave now."
                scene Rob face
                r "Mission completed"
                return

            label park2:
                scene two path
                r "Huh more people than I thought."
                r "So which one do you want?"

                menu:
                    "The old lady":
                        jump lady
                    "The little girl":
                        jump girl2

                label girl2:
                    scene small girl

                    r "hmm I have a strange feeling about this one."
                    r "I have heard some rumors about mutated people and otherworldy beings but only in the city so we should be fine."
                    r "This is your call though fellow robber."


                    menu:
                        "Return home":
                            jump home21
                        "Continue":
                            jump Continue2
                    label home21:
                        scene first h
                        show r icon1

                        r "We gotta go or I will starve to death."
                        scene Map

                        menu:


                            "Stay home":
                                jump home22
                        label home22:
                            scene first h
                            show r icon1
                            r "Arghhh"
                            scene Bad end
                            x "So Tasty..."
                        return



                    label Continue2:
                        scene Bad endp

                        r "Ah shit."
                        r "Ehm hello there...."
                        r "Do you have some money?"
                        x "H"
                        x "E"
                        x "L"
                        x "L"
                        x "O"
                        r "What are you doing out here?"
                        x "Searching..."
                        r "For what?"
                        x "Flesh.."

                        menu:
                            "Run":
                                jump Run2
                            "Stay":
                                jump Stay2
                        label Run2:
                            scene Bad end
                            x "Runners huh..."
                            return
                        label Stay2:

                            x "I have... A deal for you."
                            r "Tell me about it"
                            x "You give me Flesh.. I give you money."
                            r "Sounds great, I will do it"
                            x "Perfect.."
                            x "You may leave now before I lose.. My last bit of humanity...."

                            menu:
                                "Going after the old lady":
                                    jump old12
                                "Return Home":
                                    jump home32
                            label old12:
                                scene old lady
                                l "Do not steal my money!"
                                r "I am afraid it will be more than just your money granny."
                                l "Oh noo!"
                                scene Bad endm
                                x "Thank you."
                                x "Go home and look in your garage, you will find your reward there."
                                r "okay"
                                scene first h
                                r "I am just glad we got out alive"
                                r "I wonder if that creature gave us something"
                                show r icon1
                                r "Holy shit"
                                scene first h2
                                r "I got my precious car back and a lot of money"
                                r "How did that creature know where I live and how my car looked like?"
                                r "I think I need to move away from here tomorrow."
                                r "Thank you for the help fellow robber."
                                scene Rob face
                                r "hehe..."
                                with dissolve
                                return

                            label home32:
                                scene Bad end
                                x "Did you really think I would let you off that easily?"
                                return


    label Park:
        r "good choice."
        r "There is always someone at the park even around 8 pm."
        scene two path
        r "Huh more people than I thought."
        r "So which one do you want?"

        menu:
            "The old lady":
                jump lady
            "The little girl":
                jump girl

        label lady:
            scene old lady
            r "Give me your money Grandma."
            l "Just take it and leave me alone."
            r "Okay Grandma."
            scene Rob face
            r "Mission completed"
            return

        label girl:
            scene small girl

            r "hmm I have a strange feeling about this one."
            r "I have heard some rumors about mutated people and otherworldy beings but only in the city so we should be fine."
            r "This is your call though fellow robber."


            menu:
                "Return home":
                    jump home
                "Continue":
                    jump Continue
            label home:
                scene first h
                show r icon1

                r "We gotta go or I will starve to death."
                scene Map

                menu:
                    "Go to the city":
                        jump city2
                    "Stay home":
                        jump home2
                label home2:
                    scene first h
                    show r icon1
                    r "Arghhh"
                    scene Bad end
                    x "So Tasty..."
                return

                label city2:
                    r "Might be some weird people around here so be careful."
                    scene the city
                    r " Well there is a homeless and a bank, which one do you want to go for fellow robber?"

                    menu:
                        "Go for the homeless":
                            jump homeless2
                        "Go inside the bank":
                            jump bank2
                    label homeless2:
                        scene homeless
                        h "What are you doing out here boy"
                        r "Just walking by."
                        h "Do not try anything funny or you will have a bullet through your head."
                        r "Relax."
                        menu:
                            "Go Inside the bank":
                                jump bank2

            label Continue:
                scene Bad endp

                r "Ah shit."
                r "Ehm hello there...."
                r "Do you have some money?"
                x "H"
                x "E"
                x "L"
                x "L"
                x "O"
                r "What are you doing out here?"
                x "Searching..."
                r "For what?"
                x "Flesh.."

                menu:
                    "Run":
                        jump Run
                    "Stay":
                        jump Stay
                label Run:
                    scene Bad end
                    x "Runners huh..."
                    return
                label Stay:

                    x "I have... A deal for you."
                    r "Tell me about it"
                    x "You give me Flesh.. I give you money."
                    r "Sounds great, I will do it"
                    x "Perfect.."
                    x "You may leave now before I lose.. My last bit of humanity...."

                    menu:
                        "Going after the old lady":
                            jump old1
                        "Return Home":
                            jump home3
                    label old1:
                        scene old lady
                        l "Do not steal my money!"
                        r "I am afraid it will be more than just your money granny."
                        l "Oh noo!"
                        scene Bad endm
                        x "Thank you."
                        x "Go home and look in your garage, you will find your reward there."
                        r "okay"
                        scene first h
                        r "I am just glad we got out alive"
                        r "I wonder if that creature gave us something"
                        show r icon1
                        r "Holy shit"
                        scene first h2
                        r "I got my precious car back and a lot of money"
                        r "How did that creature know where I live and how my car looked like?"
                        r "I think I need to move away from here tomorrow."
                        r "Thank you for the help fellow robber."
                        scene Rob face
                        r "hehe..."
                        with dissolve
                        return

                    label home3:
                        scene Bad end
                        x "Did you really think I would let you off that easily?"
                        return










    scene Rob face
    r "hehe..."
    with dissolve

    # This ends the game.

    return