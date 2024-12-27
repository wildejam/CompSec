from collections import Counter

alphabetFreq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"

key1 = "yz"
key2 = "xyz"
key3 = "wxyz"
key4 = "vwxyz"
key5 = "uvwxyz"

ciphertext1 = "csfharjzuzlcsmgucqqhrxnnjhahcruzpmgmesmccecmbzqxqsclwnsmcdbsmaczzkcsmsfhljjhidymysrzajcqymbsfzrhlbjtbdqtlccqqsymbhlfrdaglhotcrrgysazlactqdbsmbmlnqmlgrcrcbsqgswgmvcucqsrgmesfnqdrdaglhotcrgmrgcqczjvmqjckzwugnjzrdrgckyvmqrgctlhtdprgswrptjdqzlcgskzwactldrggbyksmbdprmlcbgqatkrrzlbcrcucmnqmagmeemqudyjldqrcrkzwqcrskrhlrcucqcocmykrhcrsornymbhlbjtbhlfcwntjrgnlbgugkdhldqzlchzgkrhkdmtpomkgbwhldcbqhqsfzrxmtktqspdqocbrsfdnqguybwzlcnqmocqrxphegrrmemsfdprysykjsglcrmqckqdwnsvgkjeyhjsfdansqqdybrhlfjzueskjxymbdrggbykjxgrwnsqpdqommqhzhjhrxazpddtjkwqczbsfdankosscqdqytbzlcyasrczasaeyzyecccqykqsyssscsfzrapnycjxaqglgmykgycrankosscqgmrqsrgnlsfhqhqnldmeqdtdpzjkyvqsfzrfmucqlgybihlfsmbdprrzlcugysrgckyvnqmggagsqhdhlcmtzsudazlqcecqwnssmzlzrsmqldwojdyrcqcugduhrrqomkgbgdqnlqcrnnlrgajdsrcndscbfmmkmfwqcrmtpbcrymbbydlrnnjhaxbnatkdlsqemqetgcckgmcranlbcqlhlfnqmocq"
ciphertext2 = "brgfariyvxlcrlhscqpgsvnnigbfcrtyqkgmdrnaceblcxqxprdjwnrldbbslzdxzkbrnqfhkikfidxlzqrzzidoymargxrhkakrbdpsmacqprzkbhkesbagkgprcrqfzqazkzdrqdarnzmlmpnjgrbqdzsqfrxemvbtdosrflfqfnpcsbagkgprcrflsecqbyktmqiblxwufmkxrdqfdiyvlpsectkgubprfrxppticrxlcfrlxwabsmbrgfazismacqpmlbahoatjqsxlbbqdscmmpnygmddnoudximbqrbqlxwqbqtirhkqdscqbndkykqgdpsoqmzkbhkakrbhkeduntiqhllbfthidhkcrxlcgyhirhjcnrpoljhzwhkcdzqhprgxrxlslrqsocrmcbqrgbnqftzzwzkboomobpsvphdfspmelrgbprxrzijsfkdpmqbjrbwnruhijexgkqfdzmtoqdxasflfiyvcskiwzkbdqfhzykiwhpwnrpqbqollrfzhigsvazocerjkvpdxbsecblkorrdodqxscxlcxztpczzrbcyzxddacqxjrqysrrdqfzqzqlyciwboglflzigybqblkorrdogmqptpgnkrgfqhpmmbmepcubpzijztqseysdmubpmeybhgmdsmacqprzkbveysqfdiyvmpnegafrrfdhkbnrzstcbxlqbddownrrnxlzqrnoldvnkbyrbpdsgdtgspqoljhzgdpmmocrmmmpgaictpcncrdzfmljndwqbqnrpbbqzkbbxcmpnnigbvbnzslblspdnoetfbdigmbqbllbbpmflfmpnmcq"
ciphertext3 = "aqfhypjzsxlcqkguaoqhpvnnhfahapuznkgmcqmcaccmzxqxoqclulsmabbskyczxicskqfhjhjhgbymwqrzyhcqwkbsdxrhjzjtzbqtjacqoqymzflfpbagjfotaprgwqazjyctobbskzmllomlepcrazsqeqwgktcuaosrekesdlqdpbagjfotapgmpecqaxjvkojcixwueljzpbrgaiyvkorgarlhrbpreqwrnrjdoxlceqkzuyctjbrgezykqkbdnpmlazgqyrkrpxlbapcuaknqkygmccmqsbyjjbqrapkzuocrqirhjpcuaocoakykpfcrqmrnwkbhjzjtzflfaunthpgnjzgueidhjbqzjahzeirhibmtnmmkezwhjbcbofqsdxrxkrktoqpdomcbpqfdloguwzwzjanqkmcqpvphcerrkcmsdbprwqykhqglapmqaiqdulsveijewfjsdbanqoqdwzrhjdjzscskhvymzbrgezykhvgrulsqnbqokkqhxfjhpvaznbdthiwqaxbsdbanimssaodqwrbzjayaqpczyqaewxyeaacqwiqswqssaqfzpypnwajxyoglekykewcrylkoqqcqekrqqpgnjqfhofqnjbmeobtdnxjkwtqsdxrfkscqjeybgflfqkbdnprzjaugwqrgaiyvlomgeygsofdhjamtxqudyxlqaccqulsskxlzpqmqjbwohbyraocuebuhppqokigbebqnjocrlllreyjdqpcnbqcbdkmkkdwqapmtnzcrwkbbwblrlljhyvbnyrkdjqqekoeteackekcryllbaolhjdnqkmcq"
ciphertext4 = "zpegbnhxuzizrlhqaoqhoummkdyfcrrwolhicqmczbblcvovqszivmtiabbsjxbyagaqmscekikdgbymvpqybfaoymypeysdjzjtyapsmyaoqsvjagmbpbagiensdnpeysxwkzdpobbsjylkomkjgrzobatmeqwgjsbtdmqpgmbpemrzpbagiensdnekrgznbykrkojchwvthjhxrdodbjzrkorgzqkguznpgstooskzoxlcdpjyxwarldodfazgqkbdmolkdxeoathoqymxapcuzjmpnwekeejntczfjbqrzojyxmapskoekqdqaocozjxjsdapsookxlcdjzjtyekedslrjrdkkahqeidhiapymyfxgkoejcnpnmmkdyvgmzazqhnpeystkrktnpocrkazrscamphqwzwzizmpnkaorxmedfsnkcmscaoqzowijsdibqnmaiqdtkruhghcyhgpecbjqoqdvyqgmbhxuephiwzizbrgdyxjktepwnpnocrkkkqhweigstyxpdaqijxmaxbscazmlkqqcqanxscvjayapobyboycyzvbbbdmwiqsvprrdodxramkxbktyogldjxjhuapanhlrrdmekrqpofmmodfqhnkkcnaobtdmwijzroqfzocltdmjeybfeketizbprowkbvcwqrgzhxuomkegadppgedjamtwptcbvjoceznvmtokxlzoplpmzumjdvobpdqebuhoopnngezgdnkkpdnlllrdxictnaldszyelngkdwqzolsqxapymyyxcmnlljhxuambpiblsnblpfpeackdjbqbjjzcqiekeomkmcq"
ciphertext5 = "yodfarfvsxlcoiescqmdpvnnfdyfcrqvnkgmaokaceyizxqxmoajwnoiabbsiwaxzkyokqfhhfhfiduiwqrzwfaoymxodxrhhxhrbdmpjacqmowkbhhbpbaghdmrcrncwqazhwarqdxokzmljmkjgrynazsqcouemvyqaosrcicqfnmzpbaghdmrcrcipecqyvhtmqfyixwucjhxrdncaiyvimpecthdrbprcoupptfzoxlccoixwaypjbrgcxwismxznpmlyxeoatgnpxlbynascmjmkygmaakoudufjbqrynixwqynqirhhnascqykakykndapsonjwkbhhxhrbhhbauntfnellbcqeidhhzoxlcdveirhgzkrpoigezwhhzazqhmodxrxipirqslzomcbnodbnqcqwzwzhylomoympvphacppmeiodbpruowijschapmqygobwnoreijeudhqfdwjqoqduxpflffvscskftwkbdncezykftepwnomnbqoiiofzhfdpvazlzbrjksmaxbsbzylkoooaodqupzxlcuwqpczwoycyzuaaacqugoqysooaqfznwnlycftyoglciwigyynylkoooaogmnmqpgnhodfqhmjjbmemzrbpzfgwtqsbvpdmuymjeybedjdsmxznprzhyseysncaiyvjmkegacoofdhhykrzsqzyxlqyaaownookxlznokoldskhbyrymasgdqdppqoigezgdmjjocrjjjpgafzqpcnzoazfmigkdwqynkrpbynwkbbuzjpnnfdyvbnwpiblsmakoetcyaigmynyllbymjflfjmkmcq"

ciphertexttest = 'SIJHNUWCYGYSZGSZJHVVUIECSLKKSNCFIERFUGYTFFIKAVUFITUTDAKVCEUHIUVVVKOAUQCKGCEEWWDGAOGXHFPTYYDHZOBSKQCKUAOGRFDAIRFWVVTTAPPWJUTEZZOEVLDKRGRAAOPRIYQDSFUFPKHMRECLVAHVVHLRPDDLGKCREZPOUGPNKKWEMPNXWVRVFOLZSIGZIIKSETFPCHOJGMOIJSKVOENRFUUPSRLRNJPCYKOMGUORSDCKJAKLCEYOAKHJVTAOPRISWAITDBKHVRXHHKJLMDLGJUAAGOSKQUSRLRZKHMJLFYGURPVTIKLNUDBUJPSNHZWCYEZVOMGYYTOCJGJOEFSIPVFDLBVVLLCPSNJFIKZOJVOAKBCLYLRVVCVCNEIWVRVZIIKSETFSYRICFYEKXFEVVLFQRFPHWFPOEUDHZPRIYHTJRBNJLNPRIBPVWDHPVVAEIBCLYPLCXBUGYSKDBUVOAKLQRPUOKDZNCFSXLJVTLAJRBJHVRNKOKKZAPRFUQUOERWIGTEDESIVOEKKFZNSIEBCLTCOZFSZTLMVPPVTAHVOCFMPNPRIIGFEJSZVCZEGOSRULBVIFRPRWZWVDGTIJVGKCWLVWCEHVRVYSIUPNTHWYCCESHSEJLRVLVRXLBVHBTQUSTLCLUVFJKOUQDSROZIQBNUPSCKMEYDGSGJODHZZMLTYDHXTLAKJFZOWEEPWIGDIKKZZVALVJFVGUPRWQYGZEMHFPYOEIHWEVVWYLQYQUEDDMJKUKRQRNKAHERULKKEKRDFKUTKKSKTHCBWSCNTEKKSEYOAKLHNCZTYDHPQBMVDBKCUDZZWCNWRFPWJGAOTRBMGFYFXFNCYNZQUKQZIIKSETFAEHLGTLSJLCEQMIIUSJQSUKLCERHSJHRWQYAELBJVHNKRJVTOEIIOTGIUKKSIGFEJKOUJHRUHBVFHGRLBNJLNJKSRPZWVUSUOLYFXARMLTFRALEOOWLHUTDAKVCEUHIUVVVOFBIRHYGYAEGWNGYEMHFPOBCYVVFEREUEMKJLDVDHYQMSZUQYCYLVVKVMUENKWDXLRPLBKKTAKHZPHVRYLGWCCOLUWKGDACNKRUVVVUHYGTOFUHFQBRYRIJGOENDGUGLPCBWDRYEJVSUYPTYWVVEBRJHKYKJHYXBXQCEIWVVHHMZOMRPKWYHBKJPSKUOXGKYTDAVKUAKXFRNSYWHZKVOAKWVVTLMLVHSGZODHUIQBNUVTFTAHVISRTZWYLQYJLHRGSORYEJVSUKDAJGWJVYEJVSUVOEIHTFTLWYHBRPVTYHFDGTBVUCWVOEWDAZNFCRPSUQDNKRZZXLHVUSRPKIWHZKVOAKKSJJVUCGPVYHREHRFHAHVGOEILRNKWTJOENLZCTBNKKOKYHSROZNJPCYLWEVLNUHRKQJOEYSPDBTNKOKKZTYHRRPNEIBCLMUONWVVUAOIBCWVOEYRIEFPDFQCKDLLZHJVKUSLFVEQUSVQGVDBTZGCZHFOLKOMGHNPLBWNBEEFSNKAHJLFYGURPWOBGOIDDKRAMRFPOGNHCVZVZEOHRVOCYHYJESVPMAKDZKQOIJIODKSYKKSNQYLULGNKKENKMJJVUCGVVYPSYWCCKCERWHYGWLRFSFHKAEJSIDLCRXGVKAIJWVVRSATHCWFHNXHFKJHTZVGZTOEEUMJPHTLUSZHLAIWVRVBNCHGJAVUTDBXKCEDHGFOLMFUSUGMIELHVKUFFUARVPOEWVRPAHZVWKYVUCGPVKTPFVGZDSEKRUVVOIDWCDQCEZFOEPVTJDMRPFTYLBXFLFZQWKGMOILRFPVTBQCNCUYKKWEIKEWLBZVLINRICFHSBBCLQUEDRFVSBEJWWFPTIJVGKCWLVWCEKMYFXAVCUTERAFTLTYDBKJPSNKSEAVUWLFJVZPFNSKQTENKMJJVUCGMFWUOKZWJJFOLUPIQAHVUHFQCEIKSRTDHRWMFWZAZGHYGYEZVBFVOIEJHFYOITKVVQYAEBCEGLLJHQFWSDFEXVEAMPEFFVOEILGMGYYRQLZQBSKRVRXL'
ciphertexttest = ciphertexttest.lower()

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

# def pop_var_dict(dict):
#     """Calculate population variance of letter frequencies given a dictionary of frequencies"""
#     freqs = dict
#     mean = sum(float(v) for v in freqs.values())/len(freqs)  
#     return sum((float(freqs[c])/len(dict)-mean)**2 for c in freqs)/len(freqs)

def calcPopVarVigenere(inputString, keyLength):
    finalPopVar = 0
    subStringArr = []
    for i in range(0, keyLength):
        subStringArr += [""]
    j = 0
    for char in inputString:
        subStringArr[j] += char
        j = (j + 1) % keyLength

    for subStr in subStringArr:
        finalPopVar += pop_var(subStr)
    finalPopVar /= keyLength
    return finalPopVar

def calcFreqVigenere(inputString, keyLength):
    subStringFreqs = []
    subStringArr = []
    for i in range(0, keyLength):
        subStringArr += [""]
    j = 0
    for char in inputString:
        subStringArr[j] += char
        j = (j + 1) % keyLength

    for subStr in subStringArr:
        freqs = Counter(subStr)
        k = {}
        for i in alphabet.lower():
            if i in list(freqs.keys()):
                k.update({i: freqs[i] / len(subStr)})
            else:
                k.update({i: 0})
        subStringFreqs.append(k)

    return subStringFreqs

# def decrypt(ciphertext, inputKey):
#     plaintext = ""
#     i = 0
#     for char in ciphertext:
#         shift = 26 - (ord(inputKey[i]) - 65)
#         negShift = shift - 26
#         plaintext += alphabet[ord(char) - 97 + negShift]
#         i = (i + 1) % len(inputKey)
    
#     return plaintext

# def checkIfIsEnglishWords(plaintext, wordList):
#     plaintextCrawler = 0
#     testedWord = ""
#     testedLen = 10
#     hasFailed = False
#     while plaintextCrawler < 100:
#         testedWord = plaintext[plaintextCrawler : plaintextCrawler + testedLen]
#         if testedLen <= 0:
#             hasFailed = True
#             break
#         elif (testedWord + "\n") in wordList:
#             print(testedWord)
#             plaintextCrawler += testedLen
#             testedLen = 10
#         else:
#             testedLen -= 1

#     return not hasFailed

def checkCloseness(dict1Lst, dict2Lst):
    differenceValue = 0
    
    i = 0
    for dict1Value in dict1Lst:
        print(dict1Lst)
        print(dict2Lst)
        differenceValue += abs(dict1Value - dict2Lst[i])
        i += 1
    
    return differenceValue


keyLength = 0
key = ""

for i in range(2,13):
    popVar = calcPopVarVigenere(ciphertexttest, i)
    if popVar > 0.001:
        keyLength = i
        break

subStrFreqs = calcFreqVigenere(ciphertexttest, keyLength)

# for freqDictionary in subStrFreqs:
#     print(freqDictionary)
#     mostCommonChar = max(freqDictionary, key=freqDictionary.get)
#     shift = alphabet[(ord(mostCommonChar) - 97) - 4]
#     key += shift

for freqDictionary in subStrFreqs:
    differencesList = []
    freqDictList = list(freqDictionary.values())
    alphabetList = list(alphabetFreq.values())

    for i in range(0, 26):
        differencesList.append(checkCloseness(freqDictList, alphabetList))
        freqDictList.append(freqDictList.pop(0))

    key += chr(differencesList.index(min(differencesList)) + 65)

print(key)