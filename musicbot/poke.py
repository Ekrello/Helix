"""
This will be added eventually, i havent gotten around to implimenting it because its non-essentiall or requested
"""


def convert(name):
    poke = """
BULBASAUR 001
IVYSAUR 002
VENUSAUR 003
CHARMANDER 004
CHARMELEON 005
CHARIZARD 006
SQUIRTLE 007
WARTORTLE 008
BLASTOISE 009
CATERPIE 010
METAPOD 011
BUTTERFREE 012
WEEDLE 013
KAKUNA 014
BEEDRILL 015
PIDGEY 016
PIDGEOTTO 017
PIDGEOT 018
RATTATA 019
RATICATE 020
SPEAROW 021
FEAROW 022
EKANS 023
ARBOK 024
PIKACHU 025
RAICHU 026
SANDSHREW 027
SANDSLASH 028
NIDORAN♀ 029
NIDORINA 030
NIDOQUEEN 031
NIDORAN♂ 032
NIDORINO 033
NIDOKING 034
CLEFAIRY 035
CLEFABLE 036
VULPIX 037
NINETALES 038
JIGGLYPUFF 039
WIGGLYTUFF 040
ZUBAT 041
GOLBAT 042
ODDISH 043
GLOOM 044
VILEPLUME 045
PARAS 046
PARASECT 047
VENONAT 048
VENOMOTH 049
DIGLETT 050
DUGTRIO 051
MEOWTH 052
PERSIAN 053
PSYDUCK 054
GOLDUCK 055
MANKEY 056
PRIMEAPE 057
GROWLITHE 058
ARCANINE 059
POLIWAG 060
POLIWHIRL 061
POLIWRATH 062
ABRA 063
KADABRA 064
ALAKAZAM 065
MACHOP 066
MACHOKE 067
MACHAMP 068
BELLSPROUT 069
WEEPINBELL 070
VICTREEBEL 071
TENTACOOL 072
TENTACRUEL 073
GEODUDE 074
GRAVELER 075
GOLEM 076
PONYTA 077
RAPIDASH 078
SLOWPOKE 079
SLOWBRO 080
MAGNEMITE 081
MAGNETON 082
FARFETCH'D 083
DODUO 084
DODRIO 085
SEEL 086
DEWGONG 087
GRIMER 088
MUK 089
SHELLDER 090
CLOYSTER 091
GASTLY 092
HAUNTER 093
GENGAR 094
ONIX 095
DROWZEE 096
HYPNO 097
KRABBY 098
KINGLER 099
VOLTORB 100
ELECTRODE 101
EXEGGCUTE 102
EXEGGUTOR 103
CUBONE 104
MAROWAK 105
HITMONLEE 106
HITMONCHAN 107
LICKITUNG 108
KOFFING 109
WEEZING 110
RHYHORN 111
RHYDON 112
CHANSEY 113
TANGELA 114
KANGASKHAN 115
HORSEA 116
SEADRA 117
GOLDEEN 118
SEAKING 119
STARYU 120
STARMIE 121
MR. MIME 122
SCYTHER 123
JYNX 124
ELECTABUZZ 125
MAGMAR 126
PINSIR 127
TAUROS 128
MAGIKARP 129
GYARADOS 130
LAPRAS 131
DITTO 132
EEVEE 133
VAPOREON 134
JOLTEON 135
FLAREON 136
PORYGON 137
OMANYTE 138
OMASTAR 139
KABUTO 140
KABUTOPS 141
AERODACTYL 142
SNORLAX 143
ARTICUNO 144
ZAPDOS 145
MOLTRES 146
DRATINI 147
DRAGONAIR 148
DRAGONITE 149
MEWTWO 150
MEW 151
"""
    name = name.upper()
    name = name + " "
    ml = [line for line in poke.split('\n') if (name) in line]
    ml = str(ml)
    if ml == "[]":
        print("[ERROR]no result")
        return
    if "," in ml:
        print("[ERROR]multiple results")
        return
    line = ml.replace("']","")
    line = line.replace("['","")
    number = line.replace(name,"")
    print(number)
    return(number)

def create(number1, number2):
    import webbrowser
    url = "http://images.alexonsager.net/pokemon/fused/"
    ext = ".png"
    n1 = str(number1)
    n2 = str(number2)
    url = url + n1 + "/" + n1 + "." + n2 + ext
    print (url)
    return (url)
