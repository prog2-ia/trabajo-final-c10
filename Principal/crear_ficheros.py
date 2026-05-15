import pickle

# Base de datos de jugadores de eSports conocidos
# Formato: (nick, nombre, apellidos, edad, pais)
jugadores_data = [
    # League of Legends
    ("Faker", "Lee", "Sang-hyeok", 28, "Corea del Sur"),
    ("Caps", "Rasmus", "Borregaard", 24, "Dinamarca"),
    ("Jankos", "Marcin", "Jankowski", 29, "Polonia"),
    ("Rekkles", "Martin", "Larsson", 28, "Suecia"),
    ("Perkz", "Luka", "Perkovic", 25, "Croacia"),
    ("Uzi", "Jian", "Zi-Hao", 27, "China"),
    ("Rookie", "Song", "Eui-jin", 27, "Corea del Sur"),
    ("TheShy", "Kang", "Seung-lok", 25, "Corea del Sur"),
    ("Ruler", "Park", "Jae-hyuk", 25, "Corea del Sur"),
    ("Chovy", "Jeong", "Ji-hoon", 24, "Corea del Sur"),
    ("Gumayusi", "Lee", "Min-hyeong", 22, "Corea del Sur"),
    ("Keria", "Ryu", "Min-seok", 22, "Corea del Sur"),
    ("Zeus", "Choi", "Woo-je", 20, "Corea del Sur"),
    ("Oner", "Moon", "Hyeon-jun", 21, "Corea del Sur"),
    ("BeryL", "Cho", "Geon-hee", 24, "Corea del Sur"),
    ("Xiaohu", "Li", "Yuan-Hao", 24, "China"),
    ("GALA", "Chen", "Wei", 22, "China"),
    ("Ming", "Shi", "Sen-Ming", 26, "China"),
    ("369", "Bai", "Jia-Hao", 24, "China"),
    ("Karsa", "Hong", "Hao-Hsuan", 28, "Taiwán"),

    # CS:GO / CS2
    ("s1mple", "Oleksandr", "Kostyliev", 27, "Ucrania"),
    ("ZywOo", "Mathieu", "Herbaut", 23, "Francia"),
    ("NiKo", "Nikola", "Kovac", 27, "Bosnia"),
    ("device", "Nicolai", "Reedtz", 28, "Dinamarca"),
    ("electronic", "Denis", "Sharipov", 27, "Rusia"),
    ("coldzera", "Marcelo", "David", 29, "Brasil"),
    ("fer", "Fernando", "Alvarenga", 30, "Brasil"),
    ("FalleN", "Gabriel", "Toledo", 32, "Brasil"),
    ("kennyS", "Kenny", "Schrub", 29, "Francia"),
    ("GuardiaN", "Ladislav", "Kovacs", 32, "Eslovaquia"),
    ("rain", "Håvard", "Nygaard", 30, "Noruega"),
    ("olofmeister", "Olof", "Kajbjer", 31, "Suecia"),
    ("GeT_RiGhT", "Christopher", "Alesund", 32, "Suecia"),
    ("f0rest", "Patrik", "Lindberg", 33, "Suecia"),
    ("flusha", "Robin", "Ronnquist", 31, "Suecia"),
    ("ropz", "Robin", "Kool", 24, "Estonia"),
    ("broky", "Helvijs", "Saukants", 23, "Letonia"),
    ("blameF", "Benjamin", "Bremer", 26, "Dinamarca"),
    ("karrigan", "Finn", "Andersen", 33, "Dinamarca"),
    ("Twistzz", "Russel", "Van Dulken", 24, "Canadá"),

    # Valorant
    ("TenZ", "Tyson", "Ngo", 23, "Canadá"),
    ("Shroud", "Michael", "Grzesiek", 30, "Canadá"),
    ("cNed", "Mehmet", "Yagiz", 23, "Turquía"),
    ("Derke", "Nikita", "Sirmitev", 22, "Finlandia"),
    ("Aspas", "Eirik", "Mikkel", 23, "España"),
    ("Chronicle", "Timofey", "Khromov", 22, "Rusia"),
    ("Shao", "Dmitry", "Dvoeglazov", 22, "Rusia"),
    ("Alfajer", "Emir", "Ali Beder", 18, "Turquía"),
    ("Leo", "Leo", "Jannesson", 21, "Suecia"),
    ("nAts", "Ayaz", "Akhmetshin", 23, "Rusia"),

    # Dota 2
    ("N0tail", "Johan", "Sundstein", 30, "Dinamarca"),
    ("Puppey", "Clement", "Ivanov", 33, "Estonia"),
    ("Miracle", "Amer", "Al-Barkawi", 27, "Jordania"),
    ("Ana", "Anathan", "Pham", 24, "Australia"),
    ("Ceb", "Sébastien", "Debs", 31, "Francia"),
    ("Fly", "Tal", "Aizik", 29, "Israel"),
    ("SumaiL", "Sumail", "Hassan", 25, "Pakistán"),
    ("Matumbaman", "Lasse", "Urpalainen", 29, "Finlandia"),
    ("JerAx", "Jesse", "Vainikka", 30, "Finlandia"),
    ("Topson", "Topias", "Taavitsainen", 25, "Finlandia"),

    # Fortnite / Battle Royale
    ("Bugha", "Kyle", "Giersdorf", 21, "EEUU"),
    ("Aqua", "David", "Wang", 22, "Austria"),
    ("Mongraal", "Kyle", "Jackson", 20, "Reino Unido"),
    ("benjyfishy", "Benjy", "Fish", 20, "Reino Unido"),
    ("MrSavage", "Martin", "Foss", 21, "Noruega"),

    # Street Fighter / Fighting
    ("Tokido", "Hajime", "Taniguchi", 38, "Japón"),
    ("Daigo", "Daigo", "Umehara", 42, "Japón"),
    ("Punk", "Victor", "Woodley", 26, "EEUU"),
    ("Infiltration", "Lee", "Seon-woo", 37, "Corea del Sur"),
    ("Momochi", "Yusuke", "Momochi", 36, "Japón"),

    # Rocket League
    ("jstn", "Justin", "Morales", 22, "EEUU"),
    ("Garrett", "Garrett", "Gordon", 23, "EEUU"),
    ("Arsenal", "Tshaka", "Taylor", 24, "EEUU"),
    ("Firstkiller", "Mariano", "Arruda", 21, "Brasil"),
    ("Scrub Killa", "Kyle", "Robertson", 22, "Escocia"),
    ("Fairy Peak", "Victor", "Locquet", 24, "Francia"),
    ("Vatira", "Yanis", "Darras", 20, "Francia"),
    ("Moist", "Nicholas", "Quaye", 22, "Ghana"),
    ("Chronic", "Kris", "Hamann", 23, "Alemania"),
    ("Kassio", "Kévin", "Afonso", 23, "Francia"),

    # Overwatch
    ("Profit", "Park", "Joon-yeong", 25, "Corea del Sur"),
    ("Fleta", "Kim", "Byung-sun", 25, "Corea del Sur"),
    ("Carpe", "Lee", "Jae-hyeok", 25, "Corea del Sur"),
    ("Pine", "Kim", "Do-hyeon", 27, "Corea del Sur"),
    ("Gesture", "Hong", "Jae-hee", 24, "Corea del Sur"),
    ("Bdosin", "Choi", "Seung-tae", 24, "Corea del Sur"),
    ("Fissure", "Chan-hyung", "Baek", 27, "Corea del Sur"),
    ("Rein", "Kim", "Hyun-woo", 24, "Corea del Sur"),
    ("Saebyeolbe", "Park", "Jong-ryeol", 26, "Corea del Sur"),
    ("Libero", "Kim", "Hye-sung", 23, "Corea del Sur"),
]

# Base de datos de equipos de eSports conocidos
# Formato: (nombre, region)
equipos_data = [
    # League of Legends
    ("T1", "Corea"),
    ("Gen.G", "Corea"),
    ("Cloud9", "Norteamérica"),
    ("Team Liquid", "Norteamérica"),
    ("Fnatic", "Europa"),
    ("G2 Esports", "Europa"),
    ("100 Thieves", "Norteamérica"),
    ("Evil Geniuses", "Norteamérica"),
    ("NRG", "Norteamérica"),
    ("KT Rolster", "Corea"),
    ("DragonX", "Corea"),
    ("Royal Never Give Up", "China"),
    ("Edward Gaming", "China"),
    ("JDG Gaming", "China"),
    ("Bilibili Gaming", "China"),
    ("Weibo Gaming", "China"),
    ("Vitality", "Europa"),
    ("MAD Lions", "Europa"),
    ("Astralis", "Europa"),
    ("SK Telecom T1", "Corea"),

    # CS:GO
    ("Natus Vincere", "CIS"),
    ("FaZe Clan", "Internacional"),
    ("Team Vitality", "Europa"),
    ("Heroic", "Europa"),
    ("ENCE", "Europa"),
    ("BIG", "Alemania"),
    ("OG", "Europa"),
    ("Complexity", "Norteamérica"),
    ("FURIA", "Brasil"),
    ("Team Spirit", "CIS"),
    ("Gambit Esports", "CIS"),
    ("NIP", "Suecia"),
    ("mousesports", "Europa"),
    ("Virtus.pro", "CIS"),
    ("Team One", "Brasil"),

    # Valorant
    ("Sentinels", "Norteamérica"),
    ("LOUD", "Brasil"),
    ("FNATIC", "EMEA"),
    ("Paper Rex", "Pacífico"),
    ("DRX", "Corea"),
    ("ZETA DIVISION", "Japón"),
    ("KRÜ Esports", "Latinoamérica"),
    ("Team Secret", "Pacífico"),
    ("XSET", "Norteamérica"),
    ("OpTic Gaming", "Norteamérica"),

    # Dota 2
    ("OG", "Europa"),
    ("Team Secret", "Europa"),
    ("PSG.LGD", "China"),
    ("Evil Geniuses Dota", "Norteamérica"),
    ("Virtus.pro Dota", "CIS"),
    ("Liquid Dota", "Europa"),
    ("Alliance", "Europa"),
    ("Newbee", "China"),
    ("Wings Gaming", "China"),
    ("Vici Gaming", "China"),

    # Rocket League
    ("NRG Rocket League", "Norteamérica"),
    ("Team BDS", "Europa"),
    ("Moist Esports", "Europa"),
    ("Complexity RL", "Norteamérica"),
    ("G2 RL", "Norteamérica"),
    ("Renault Vitality RL", "Europa"),
    ("Faze RL", "Norteamérica"),
    ("Spacestation Gaming", "Norteamérica"),
    ("Wolves Esports", "Europa"),
    ("Endpoint", "Europa"),
]

# Creamos el fichero de jugadores
with open('jugadores.pickle', 'wb') as f:
    pickle.dump(jugadores_data, f)

# Creamos el fichero de equipos
with open('equipos.pickle', 'wb') as f:
    pickle.dump(equipos_data, f)

print("Ficheros creados correctamente: jugadores.pickle y equipos.pickle")