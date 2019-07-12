from __future__ import unicode_literals

from django.db import models
#
#
# class AccountInfo(models.Model):
#     pid = models.IntegerField()
#     acc_type = models.CharField(max_length=100)
#     activation_code = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'account_info'
#
#
# class AccountType(models.Model):
#     description = models.CharField(max_length=45)
#
#     class Meta:
#         managed = False
#         db_table = 'account_type'
#
#
# class Apikeys(models.Model):
#     parentid = models.IntegerField()
#     key = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'apikeys'
#
#
# class ArbolmusicalHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'arbolmusical_headers'
#         app_label = 'kiwi_game'
#
#
# class ArbolmusicalLevels(models.Model):
#     headerid = models.IntegerField()
#     birds = models.IntegerField()
#     nests = models.IntegerField()
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     tutorial = models.IntegerField()
#     sound = models.CharField(max_length=500)
#     birdsound = models.CharField(db_column='birdSound', max_length=500)  # Field name made lowercase.
#     time = models.IntegerField()
#     birdlistenedpre = models.CharField(db_column='birdListenedPre', max_length=500)  # Field name made lowercase.
#     birdlistened = models.CharField(db_column='birdListened', max_length=500)  # Field name made lowercase.
#     errors = models.IntegerField()
#     correct = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'arbolmusical_levels'
#         app_label = 'kiwi_game'
#
#
# class ArenamagicaHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'arenamagica_headers'
#         app_label = 'kiwi_game'
#
#
# class ArenamagicaLevels(models.Model):
#     headerid = models.IntegerField()
#     levelkey = models.CharField(max_length=100)
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     time = models.IntegerField()
#     passed = models.IntegerField()
#     repeated = models.IntegerField()
#     accuracy = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'arenamagica_levels'
#         app_label = 'kiwi_game'
#
#
# class Children(models.Model):
#     parentid = models.IntegerField()
#     name = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     dob = models.CharField(max_length=100)
#     grade = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     school = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     picture = models.CharField(max_length=100)
#     register_date = models.DateTimeField()
#     active = models.IntegerField()
#     trial_active = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'children'
#         app_label = 'kiwi_child'
#
#
# class ChildrenSuscription(models.Model):
#     cid = models.IntegerField(unique=True)
#     suscription_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'children_suscription'
#
#
# class ChildrenTowiIsland(models.Model):
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     kiwis = models.IntegerField()
#     avatar = models.CharField(max_length=100)
#     avatarclothes = models.CharField(db_column='avatarClothes', max_length=1000)  # Field name made lowercase.
#     owneditems = models.CharField(db_column='ownedItems', max_length=1000)  # Field name made lowercase.
#     activemissions = models.CharField(db_column='activeMissions', max_length=1000)  # Field name made lowercase.
#     missionlist = models.CharField(db_column='missionList', max_length=1000)  # Field name made lowercase.
#     activeday = models.IntegerField(db_column='activeDay')  # Field name made lowercase.
#     riotutorial = models.IntegerField(db_column='rioTutorial')  # Field name made lowercase.
#     tesorotutorial = models.IntegerField(db_column='tesoroTutorial')  # Field name made lowercase.
#     arbolmusicaltutorial = models.IntegerField(db_column='arbolMusicalTutorial')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'children_towi_island'
#         app_label = 'kiwi_game'
#
#
# class DondequedolabolitaHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'dondequedolabolita_headers'
#         app_label = 'kiwi_game'
#
#
# class DondequedolabolitaLevels(models.Model):
#     headerid = models.IntegerField()
#     levelkey = models.CharField(db_column='levelKey', max_length=100)  # Field name made lowercase.
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     time = models.IntegerField()
#     numofmonkeys = models.IntegerField(db_column='numOfMonkeys')  # Field name made lowercase.
#     numofobjects = models.IntegerField(db_column='numOfObjects')  # Field name made lowercase.
#     instructions = models.CharField(max_length=500)
#     numofmovements = models.IntegerField(db_column='numOfMovements')  # Field name made lowercase.
#     timeofmovements = models.CharField(db_column='timeOfMovements', max_length=100)  # Field name made lowercase.
#     correct = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dondequedolabolita_levels'
#         app_label = 'kiwi_game'
#
#
# class Feed(models.Model):
#     uid = models.CharField(max_length=11)
#     target = models.CharField(max_length=11)
#     mssg = models.CharField(max_length=1000)
#     thread = models.IntegerField()
#     type = models.CharField(max_length=100)
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'feed'
#
#
# class FreeTrial(models.Model):
#     md5_device = models.CharField(max_length=100)
#     trial_id = models.DateTimeField()
#     linked_account = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'free_trial'
#
#
# class GameAreas(models.Model):
#     game_id = models.IntegerField()
#     area = models.IntegerField()
#     subarea = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'game_areas'
#
#
# class GamesConfiguration(models.Model):
#     cid = models.IntegerField()
#     configid = models.IntegerField(db_column='configID')  # Field name made lowercase.
#     sid = models.IntegerField()
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'games_configuration'
#
#
# class GamesConfigurationFiles(models.Model):
#     sid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)
#     file = models.CharField(max_length=100)
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'games_configuration_files'
#
#
# class Institutions(models.Model):
#     name = models.CharField(max_length=200)
#     type = models.CharField(max_length=45)
#     country = models.CharField(max_length=45)
#     state = models.CharField(max_length=45)
#     website = models.CharField(max_length=45)
#     contactname = models.CharField(db_column='contactName', max_length=45)  # Field name made lowercase.
#     contactlastname = models.CharField(db_column='contactLastname', max_length=45)  # Field name made lowercase.
#     contactemail = models.CharField(max_length=45)
#     contactphone = models.CharField(db_column='contactPhone', max_length=45)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'institutions'
#
#
# class InteresadosEnSuscribirse(models.Model):
#     email = models.CharField(max_length=200)
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'interesados_en_suscribirse'
#
#
# class LinkedAccounts(models.Model):
#     vinculation_code_u1 = models.CharField(max_length=10)
#     vinculation_code_u2 = models.CharField(max_length=10)
#     auth_u1 = models.IntegerField()
#     auth_u2 = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'linked_accounts'
#         app_label = 'kiwi_lin'
#
#
# class LinkedAccountsOptions(models.Model):
#     linked_account_id = models.IntegerField()
#     cid = models.IntegerField()
#     auth = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'linked_accounts_options'
#         app_label = 'kiwi_lino'
#
#
# class PixframeCardsCodes(models.Model):
#     code = models.CharField(max_length=100)
#     used = models.IntegerField()
#     temp = models.IntegerField()
#     temp_num = models.IntegerField()
#     activation_day = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'pixframe_cards_codes'
#
#
# class PruebaConosDetails(models.Model):
#     headerid = models.IntegerField(db_column='headerId')  # Field name made lowercase.
#     cono = models.IntegerField()
#     distance = models.FloatField()
#     time = models.IntegerField()
#     state = models.CharField(max_length=200)
#     order = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'prueba_conos_details'
#
#
# class PruebaConosHeaders(models.Model):
#     name = models.CharField(max_length=500)
#     age = models.CharField(max_length=50)
#     sex = models.CharField(max_length=50)
#     routeid = models.CharField(db_column='routeId', max_length=50)  # Field name made lowercase.
#     testdate = models.DateTimeField(db_column='testDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'prueba_conos_headers'
#
#
# class PruebasHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pruebas_headers'
#
#
# class PruebasHeadersNew(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pruebas_headers_new'
#         app_label = 'kiwi_game'
#
#
# class PruebasLevels(models.Model):
#     header_id = models.IntegerField()
#     playerage = models.IntegerField(db_column='playerAge')  # Field name made lowercase.
#     birthdayofplayer = models.CharField(db_column='birthdayOfPlayer', max_length=300)  # Field name made lowercase.
#     inputagetimeofcomp = models.IntegerField(db_column='inputAgeTimeOfComp')  # Field name made lowercase.
#     playername = models.CharField(db_column='playerName', max_length=300)  # Field name made lowercase.
#     playeraddress = models.CharField(db_column='playerAddress', max_length=300)  # Field name made lowercase.
#     currentdate = models.CharField(db_column='currentDate', max_length=300)  # Field name made lowercase.
#     buytickettimeofcomp = models.IntegerField(db_column='buyTicketTimeOfComp')  # Field name made lowercase.
#     normalpackscore = models.IntegerField(db_column='normalPackScore')  # Field name made lowercase.
#     reversepackscore = models.IntegerField(db_column='reversePackScore')  # Field name made lowercase.
#     packtimeofcomp = models.IntegerField(db_column='packTimeOfComp')  # Field name made lowercase.
#     packtypeofweather = models.CharField(db_column='packTypeOfWeather', max_length=300)  # Field name made lowercase.
#     weatherobjectpacked = models.CharField(db_column='weatherObjectPacked', max_length=1000)  # Field name made lowercase.
#     objecttoremember = models.CharField(db_column='objectToRemember', max_length=1000)  # Field name made lowercase.
#     timeoflab = models.CharField(db_column='timeOfLab', max_length=1000)  # Field name made lowercase.
#     latenciesoflab = models.CharField(db_column='latenciesOfLab', max_length=1000)  # Field name made lowercase.
#     hitsoflab = models.CharField(db_column='hitsOfLab', max_length=1000)  # Field name made lowercase.
#     totalhits = models.IntegerField(db_column='totalHits')  # Field name made lowercase.
#     crossesoflab = models.CharField(db_column='crossesOfLab', max_length=1000)  # Field name made lowercase.
#     totalcrosses = models.IntegerField(db_column='totalCrosses')  # Field name made lowercase.
#     deadendsoflab = models.CharField(db_column='deadEndsOfLab', max_length=1000)  # Field name made lowercase.
#     totaldeadends = models.IntegerField(db_column='totalDeadEnds')  # Field name made lowercase.
#     airportroutetimeofcomp = models.IntegerField(db_column='airportRouteTimeOfComp')  # Field name made lowercase.
#     waitroomcorrect = models.IntegerField(db_column='waitRoomCorrect')  # Field name made lowercase.
#     waitroomincorrect = models.IntegerField(db_column='waitRoomIncorrect')  # Field name made lowercase.
#     waitroommissed = models.IntegerField(db_column='waitRoomMissed')  # Field name made lowercase.
#     timebetweenflights = models.FloatField(db_column='timeBetweenFlights')  # Field name made lowercase.
#     flyplanecorrect = models.IntegerField(db_column='flyPlaneCorrect')  # Field name made lowercase.
#     flyplaneincorrect = models.IntegerField(db_column='flyPlaneIncorrect')  # Field name made lowercase.
#     flyplanemissed = models.IntegerField(db_column='flyPlaneMissed')  # Field name made lowercase.
#     flyplanetimeforinput = models.FloatField(db_column='flyPlaneTimeForInput')  # Field name made lowercase.
#     flyplanetimeofcomp = models.IntegerField(db_column='flyPlaneTimeOfComp')  # Field name made lowercase.
#     pupcoinsmincorrect = models.IntegerField(db_column='pUpCoinsMinCorrect')  # Field name made lowercase.
#     pupcoinsminincorrect = models.IntegerField(db_column='pUpCoinsMinIncorrect')  # Field name made lowercase.
#     pupcoinsminmissed = models.IntegerField(db_column='pUpCoinsMinMissed')  # Field name made lowercase.
#     pupcoinsextracorrect = models.IntegerField(db_column='pUpCoinsExtraCorrect')  # Field name made lowercase.
#     pupcoinsextraincorrect = models.IntegerField(db_column='pUpCoinsExtraIncorrect')  # Field name made lowercase.
#     pupcoinsextramissed = models.IntegerField(db_column='pUpCoinsExtraMissed')  # Field name made lowercase.
#     coinsselected = models.CharField(db_column='coinsSelected', max_length=1000)  # Field name made lowercase.
#     pupcoinstimeofcomp = models.IntegerField(db_column='pUpCoinsTimeOfComp')  # Field name made lowercase.
#     unpackfirstobjs = models.CharField(db_column='unPackFirstObjs', max_length=1000)  # Field name made lowercase.
#     unpackcorrectsample = models.CharField(db_column='unPackCorrectSample', max_length=1000)  # Field name made lowercase.
#     unpackincorrectsample = models.CharField(db_column='unPackIncorrectSample', max_length=1000)  # Field name made lowercase.
#     unpackrepeatedsample = models.CharField(db_column='unPackRepeatedSample', max_length=1000)  # Field name made lowercase.
#     unpackfourfirstsample = models.CharField(db_column='unPackFourFirstSample', max_length=1000)  # Field name made lowercase.
#     unpackfourlastsample = models.CharField(db_column='unPackFourLastSample', max_length=1000)  # Field name made lowercase.
#     unpackgroupingsample = models.CharField(db_column='unPackGroupingSample', max_length=1000)  # Field name made lowercase.
#     unpackspacialprecisionsample = models.CharField(db_column='unPackSpacialPrecisionSample', max_length=1000)  # Field name made lowercase.
#     unpackpictime = models.IntegerField(db_column='unPackPicTime')  # Field name made lowercase.
#     unpacktimeofcomp = models.IntegerField(db_column='unPackTimeOfComp')  # Field name made lowercase.
#     unpacktotalcorrect = models.IntegerField(db_column='unPackTotalCorrect')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pruebas_levels'
#         app_label = 'kiwi_game'
#
#
# class PruebasLevelsNew(models.Model):
#     header_id = models.IntegerField()
#     playerage = models.IntegerField(db_column='playerAge')  # Field name made lowercase.
#     playerbirthday = models.CharField(db_column='playerBirthday', max_length=300)  # Field name made lowercase.
#     inputagetimeofcomp = models.IntegerField(db_column='inputAgeTimeOfComp')  # Field name made lowercase.
#     playername = models.CharField(db_column='playerName', max_length=300)  # Field name made lowercase.
#     playeraddress = models.CharField(db_column='playerAddress', max_length=300)  # Field name made lowercase.
#     playercurrentdate = models.CharField(db_column='playerCurrentDate', max_length=300)  # Field name made lowercase.
#     buytickettimeofcomp = models.IntegerField(db_column='buyTicketTimeOfComp')  # Field name made lowercase.
#     packnormalscore = models.IntegerField(db_column='packNormalScore')  # Field name made lowercase.
#     packreversescore = models.IntegerField(db_column='packReverseScore')  # Field name made lowercase.
#     packtimeofcomp = models.IntegerField(db_column='packTimeOfComp')  # Field name made lowercase.
#     weatherobjectpacked = models.CharField(db_column='weatherObjectPacked', max_length=1000)  # Field name made lowercase.
#     weathercongruence = models.IntegerField(db_column='weatherCongruence')  # Field name made lowercase.
#     lab1time = models.FloatField(db_column='lab1Time')  # Field name made lowercase.
#     lab2time = models.FloatField(db_column='lab2Time')  # Field name made lowercase.
#     lab3time = models.FloatField(db_column='lab3Time')  # Field name made lowercase.
#     lab1latency = models.FloatField(db_column='lab1Latency')  # Field name made lowercase.
#     lab2latency = models.FloatField(db_column='lab2Latency')  # Field name made lowercase.
#     lab3latency = models.FloatField(db_column='lab3Latency')  # Field name made lowercase.
#     lab1hits = models.IntegerField(db_column='lab1Hits')  # Field name made lowercase.
#     lab2hits = models.IntegerField(db_column='lab2Hits')  # Field name made lowercase.
#     lab3hits = models.IntegerField(db_column='lab3Hits')  # Field name made lowercase.
#     lab1crosses = models.IntegerField(db_column='lab1Crosses')  # Field name made lowercase.
#     lab2crosses = models.IntegerField(db_column='lab2Crosses')  # Field name made lowercase.
#     lab3crosses = models.IntegerField(db_column='lab3Crosses')  # Field name made lowercase.
#     lab1deadends = models.IntegerField(db_column='lab1DeadEnds')  # Field name made lowercase.
#     lab2deadends = models.IntegerField(db_column='lab2DeadEnds')  # Field name made lowercase.
#     lab3deadends = models.IntegerField(db_column='lab3DeadEnds')  # Field name made lowercase.
#     labxhits = models.DecimalField(db_column='labXHits', max_digits=4, decimal_places=2)  # Field name made lowercase.
#     labxcrosses = models.DecimalField(db_column='labXCrosses', max_digits=4, decimal_places=2)  # Field name made lowercase.
#     labxdeadends = models.DecimalField(db_column='labXDeadEnds', max_digits=4, decimal_places=2)  # Field name made lowercase.
#     labtimeofcomp = models.IntegerField(db_column='labTimeOfComp')  # Field name made lowercase.
#     waitroomcorrect = models.IntegerField(db_column='waitRoomCorrect')  # Field name made lowercase.
#     waitroomincorrect = models.IntegerField(db_column='waitRoomIncorrect')  # Field name made lowercase.
#     flyplanecorrect = models.IntegerField(db_column='flyPlaneCorrect')  # Field name made lowercase.
#     flyplaneincorrect = models.IntegerField(db_column='flyPlaneIncorrect')  # Field name made lowercase.
#     flyplanemissed = models.IntegerField(db_column='flyPlaneMissed')  # Field name made lowercase.
#     flyplanegreencorrect = models.IntegerField(db_column='flyPlaneGreenCorrect')  # Field name made lowercase.
#     flyplanegreenincorrect = models.IntegerField(db_column='flyPlaneGreenIncorrect')  # Field name made lowercase.
#     flyplanegreenmissed = models.IntegerField(db_column='flyPlaneGreenMissed')  # Field name made lowercase.
#     flyplanetimeofcomp = models.IntegerField(db_column='flyPlaneTimeOfComp')  # Field name made lowercase.
#     coinsmincorrect = models.IntegerField(db_column='coinsMinCorrect')  # Field name made lowercase.
#     coinsminincorrect = models.IntegerField(db_column='coinsMinIncorrect')  # Field name made lowercase.
#     coinsextracorrect = models.IntegerField(db_column='coinsExtraCorrect')  # Field name made lowercase.
#     coinsextraincorrect = models.IntegerField(db_column='coinsExtraIncorrect')  # Field name made lowercase.
#     coinsextramissed = models.IntegerField(db_column='coinsExtraMissed')  # Field name made lowercase.
#     coinspatterntype = models.IntegerField(db_column='coinsPatternType')  # Field name made lowercase.
#     coinsselected = models.CharField(db_column='coinsSelected', max_length=1000)  # Field name made lowercase.
#     coinsclicksbeforemin = models.IntegerField(db_column='coinsClicksBeforeMin')  # Field name made lowercase.
#     coinstimeofcomp = models.IntegerField(db_column='coinsTimeOfComp')  # Field name made lowercase.
#     unpackfirstcorrect = models.IntegerField(db_column='unPackFirstCorrect')  # Field name made lowercase.
#     unpacks1correct = models.IntegerField(db_column='unPackS1Correct')  # Field name made lowercase.
#     unpacks2correct = models.IntegerField(db_column='unPackS2Correct')  # Field name made lowercase.
#     unpacks3correct = models.IntegerField(db_column='unPackS3Correct')  # Field name made lowercase.
#     unpacks1incorrect = models.IntegerField(db_column='unPackS1Incorrect')  # Field name made lowercase.
#     unpacks2incorrect = models.IntegerField(db_column='unPackS2Incorrect')  # Field name made lowercase.
#     unpacks3incorrect = models.IntegerField(db_column='unPackS3Incorrect')  # Field name made lowercase.
#     unpacks1repeated = models.IntegerField(db_column='unPackS1Repeated')  # Field name made lowercase.
#     unpacks2repeated = models.IntegerField(db_column='unPackS2Repeated')  # Field name made lowercase.
#     unpacks3repeated = models.IntegerField(db_column='unPackS3Repeated')  # Field name made lowercase.
#     unpackfourfirstsample = models.CharField(db_column='unPackFourFirstSample', max_length=1000)  # Field name made lowercase.
#     unpackfourlastsample = models.CharField(db_column='unPackFourLastSample', max_length=1000)  # Field name made lowercase.
#     unpackspacialprecisionsample = models.CharField(db_column='unPackSpacialPrecisionSample', max_length=1000)  # Field name made lowercase.
#     unpacktimeofcomp = models.IntegerField(db_column='unPackTimeOfComp')  # Field name made lowercase.
#     unpackperctotalcorrect = models.DecimalField(db_column='unPackPercTotalCorrect', max_digits=4, decimal_places=2)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pruebas_levels_new'
#         app_label = 'kiwi_game'
#
#
# class QuestionarieAnswers(models.Model):
#     status_id = models.IntegerField()
#     pregunta = models.CharField(max_length=500)
#     respuesta = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'questionarie_answers'
#
#
# class QuestionarieAnswersOld(models.Model):
#     status_id = models.IntegerField()
#     pregunta = models.CharField(max_length=500)
#     respuesta = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'questionarie_answers_old'
#
#
# class QuestionarieParents(models.Model):
#     pid = models.IntegerField()
#     pregunta = models.CharField(max_length=500)
#     respuesta = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'questionarie_parents'
#
#
# class QuestionariePostAnswers(models.Model):
#     status_id = models.IntegerField()
#     pregunta = models.CharField(max_length=500)
#     respuesta = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'questionarie_post_answers'
#
#
# class RecolecciondeltesoroHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'recolecciondeltesoro_headers'
#         app_label = 'kiwi_game'
#
#
# class RecolecciondeltesoroLevels(models.Model):
#     headerid = models.IntegerField()
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     time = models.IntegerField()
#     tutorial = models.IntegerField()
#     passed = models.IntegerField()
#     playerobjects = models.CharField(db_column='playerObjects', max_length=500)  # Field name made lowercase.
#     playerobjectsquantity = models.CharField(db_column='playerObjectsQuantity', max_length=500)  # Field name made lowercase.
#     correctobjects = models.CharField(db_column='correctObjects', max_length=500)  # Field name made lowercase.
#     correctobjectsquantity = models.CharField(db_column='correctObjectsQuantity', max_length=500)  # Field name made lowercase.
#     spawnedobjects = models.CharField(db_column='spawnedObjects', max_length=500)  # Field name made lowercase.
#     spawneddistractors = models.CharField(db_column='spawnedDistractors', max_length=500)  # Field name made lowercase.
#     notsurecorrect = models.IntegerField(db_column='notSureCorrect')  # Field name made lowercase.
#     notsureincorrect = models.IntegerField(db_column='notSureIncorrect')  # Field name made lowercase.
#     minobjects = models.IntegerField(db_column='minObjects')  # Field name made lowercase.
#     maxobjects = models.IntegerField(db_column='maxObjects')  # Field name made lowercase.
#     availableobjects = models.CharField(db_column='availableObjects', max_length=500)  # Field name made lowercase.
#     availablecategories = models.CharField(db_column='availableCategories', max_length=500)  # Field name made lowercase.
#     searchorders = models.CharField(db_column='searchOrders', max_length=500)  # Field name made lowercase.
#     availabledistractors = models.CharField(db_column='availableDistractors', max_length=500)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'recolecciondeltesoro_levels'
#         app_label = 'kiwi_game'
#
#
# class RegisteredSerialCodes(models.Model):
#     serial = models.CharField(max_length=100)
#     md5_device = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'registered_serial_codes'
#
#
# class ResetPwdCodes(models.Model):
#     uid = models.IntegerField()
#     type = models.CharField(max_length=10)
#     rcode = models.CharField(max_length=100)
#     used = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'reset_pwd_codes'
#
#
# class RioHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'rio_headers'
#         app_label = 'kiwi_game'
#
#
# class RioLevels(models.Model):
#     headerid = models.IntegerField()
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     time = models.IntegerField()
#     tutorial = models.IntegerField()
#     reverse = models.IntegerField()
#     speed = models.IntegerField()
#     correctobjects = models.IntegerField(db_column='correctObjects')  # Field name made lowercase.
#     incorrectobjects = models.IntegerField(db_column='incorrectObjects')  # Field name made lowercase.
#     levelobjects = models.CharField(db_column='levelObjects', max_length=500)  # Field name made lowercase.
#     availableobjects = models.CharField(db_column='availableObjects', max_length=500)  # Field name made lowercase.
#     reverseobjects = models.CharField(db_column='reverseObjects', max_length=500)  # Field name made lowercase.
#     neutralobjects = models.CharField(db_column='neutralObjects', max_length=500)  # Field name made lowercase.
#     forceforestobjects = models.CharField(db_column='forceForestObjects', max_length=500)  # Field name made lowercase.
#     forcebeachforest = models.CharField(db_column='forceBeachForest', max_length=500)  # Field name made lowercase.
#     specialreverseobjects = models.CharField(db_column='specialReverseObjects', max_length=500)  # Field name made lowercase.
#     specialleaveobjects = models.CharField(db_column='specialLeaveObjects', max_length=500)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'rio_levels'
#         app_label = 'kiwi_game'
#
#
# class RouteConfiguration(models.Model):
#     cid = models.IntegerField()
#     routeid = models.IntegerField(db_column='routeID')  # Field name made lowercase.
#     sid = models.IntegerField()
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'route_configuration'
#
#
# class RouteConfigurationFiles(models.Model):
#     sid = models.IntegerField()
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)
#     file = models.CharField(max_length=100)
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'route_configuration_files'
#
#
# class SerialCodesPc(models.Model):
#     pid = models.IntegerField()
#     serial = models.CharField(max_length=100)
#     mail = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     id_bw = models.CharField(max_length=100)
#     card_bw = models.CharField(max_length=100)
#     ord_id_bw = models.CharField(max_length=100)
#     auth_code_bw = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'serial_codes_pc'
#
#
# class SessionType(models.Model):
#     tipo = models.CharField(max_length=40)
#
#     class Meta:
#         managed = False
#         db_table = 'session_type'
#
#
# class ShadowsHeaders(models.Model):
#     date = models.DateTimeField()
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     gametime = models.IntegerField(db_column='gameTime')  # Field name made lowercase.
#     passedlevels = models.IntegerField(db_column='passedLevels')  # Field name made lowercase.
#     repeatedlevels = models.IntegerField(db_column='repeatedLevels')  # Field name made lowercase.
#     playedlevels = models.IntegerField(db_column='playedLevels')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'shadows_headers'
#         app_label = 'kiwi_game'
#
#
# class ShadowsLevels(models.Model):
#     headerid = models.IntegerField()
#     levelkey = models.CharField(db_column='levelKey', max_length=100)  # Field name made lowercase.
#     level = models.IntegerField()
#     sublevel = models.IntegerField()
#     shadow = models.CharField(max_length=100)
#     shadowtime = models.CharField(db_column='shadowTime', max_length=100)  # Field name made lowercase.
#     numofoptions = models.IntegerField(db_column='numOfOptions')  # Field name made lowercase.
#     options = models.CharField(max_length=500)
#     correct = models.IntegerField()
#     time = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'shadows_levels'
#         app_label = 'kiwi_game'
#
#
# class Specialists(models.Model):
#     name = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     relation = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     picture = models.CharField(max_length=100)
#     active = models.IntegerField()
#     verified = models.IntegerField()
#     dob = models.CharField(max_length=100)
#     register_date = models.DateTimeField()
#     fb_id = models.CharField(max_length=200)
#     trial_active = models.IntegerField()
#     public = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'specialists'
#
#
# class TowiIndex(models.Model):
#     parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
#     cid = models.IntegerField()
#     gamekey = models.CharField(db_column='gameKey', max_length=100)  # Field name made lowercase.
#     index = models.FloatField()
#     date = models.DateTimeField()
#     serverdate = models.DateTimeField(db_column='serverDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'towi_index'
#         app_label = 'kiwi_game'
#
#
# class UserSession(models.Model):
#     user_id = models.IntegerField()
#     session_type = models.IntegerField()
#     date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'user_session'
#
#
# class UserType(models.Model):
#     description = models.CharField(max_length=45)
#
#     class Meta:
#         managed = False
#         db_table = 'user_type'
#         app_label = 'kiwi_vid'
#
#
# class Users(models.Model):
#     name = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     relation = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     picture = models.CharField(max_length=100)
#     dob = models.DateField()
#     verified = models.IntegerField()
#     register_date = models.DateTimeField()
#     fb_id = models.CharField(max_length=200)
#     user_type = models.IntegerField()
#     account_type = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#         app_label = 'kiwi_users'
#
#
# class ValidationIds(models.Model):
#     pid = models.CharField(max_length=11)
#     vcode = models.CharField(max_length=500)
#     link_id = models.CharField(max_length=10)
#
#     class Meta:
#         managed = False
#         db_table = 'validation_ids'
#         app_label = 'kiwi_vid'
#
#
# class Vinculation(models.Model):
#     parentid = models.IntegerField()
#     cid = models.IntegerField()
#     vinculation_code = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'vinculation'
#
#
# class CancelData(models.Model):
#     pid = models.IntegerField()
#     id_cancelado = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     mail = models.CharField(max_length=100)
#     id_pago_recurrente = models.IntegerField()
#     motivo = models.CharField(max_length=200)
#     message = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'cancel_data'
#
#
# class Catalogue(models.Model):
#     recurrency_id = models.IntegerField()
#     max_kids = models.IntegerField()
#     description = models.CharField(max_length=100)
#     price = models.IntegerField()
#     status = models.SmallIntegerField()
#     promocode = models.CharField(max_length=45)
#
#     class Meta:
#         managed = False
#         db_table = 'catalogue'
#
#
# class CatalogueOld(models.Model):
#     recurrency_id = models.IntegerField()
#     max_kids = models.IntegerField()
#     description = models.CharField(max_length=100)
#     price = models.IntegerField()
#     status = models.TextField()  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'catalogue_old'
#
#
# class Recurrency(models.Model):
#     recurrency_id_banwire = models.IntegerField()
#     time = models.CharField(max_length=45)
#     active = models.TextField()  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'recurrency'
#
#
# class SuscriptionData(models.Model):
#     pid = models.IntegerField()
#     type = models.IntegerField()
#     card_name = models.CharField(max_length=100)
#     card_lastname = models.CharField(max_length=100)
#     card_email = models.CharField(max_length=100)
#     id_transaccion = models.CharField(max_length=200)
#     token = models.CharField(max_length=200)
#     id_tarjeta = models.CharField(max_length=200)
#     id_pago_recurrente = models.CharField(max_length=200)
#     code = models.IntegerField()
#     fecha_de_inicio = models.DateTimeField()
#     recurrencia = models.IntegerField()
#     success = models.IntegerField()
#     blocked = models.IntegerField()
#     canceled = models.IntegerField()
#     monto = models.FloatField()
#     message = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'suscription_data'
