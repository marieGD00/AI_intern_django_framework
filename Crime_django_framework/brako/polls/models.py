from django.db import models

# Create your models here.


# exterior tables
class Ville(models.Model):
    id_ville = models.AutoField(primary_key = True)
    code_postal = models.CharField(max_length = 5)
    nom_ville = models.CharField(max_length = 50)
    nb_habitants = models.IntegerField()

    def __str__(self):
        return self.nom_ville +'\t('+self.code_postal +')'

class Securite(models.Model):
    id_secu = models.IntegerField(primary_key=True)
    alarme = models.BooleanField(default = False) 
    camera = models.BooleanField(default = False)
    sas = models.BooleanField(default = False)
    surveillance_humaine = models.BooleanField(default = False)
    dispositif_anti_braquage = models.BooleanField(default = False)

    def __str__(self):
        return 'Securite '+str(self.id_secu)+'\t:\tAlarme '+str(self.alarme)+'\tCamera '+str(self.camera)+'\tSas '+str(self.sas)+'`\tSurveillance '+str(self.surveillance_humaine)+'\tDAB '+str(self.dispositif_anti_braquage)
    
class Blesse(models.Model):
    id_blesse = models.AutoField(primary_key=True)
    criminels = models.IntegerField(default = 0)
    cibles = models.IntegerField(default = 0)
    temoins = models.IntegerField(default = 0)
    force_ordre = models.IntegerField(default = 0)

    def __str__(self):
        return 'Blessés '+str(self.id_blesse)+'\t:\tCrim. '+str(self.criminels)+'\tCibles '+str(self.cibles)+'\tTémoins '+str(self.temoins)+'\tFdO '+str(self.force_ordre)

class Source(models.Model):
    id_source = models.AutoField(primary_key = True)
    nom_source = models.CharField(max_length = 50)

    def __str__(self):
        return self.nom_source

# many-to-many relationships with braquages --> relationships will be set up later
class Braqueur(models.Model):
    id_braqueur = models.AutoField(primary_key = True)
    age = models.IntegerField(blank = True, null = True)
    
    class Visage_couvert_enum(models.TextChoices):
        DECOUVERT = 'D'
        COUVERT = 'C'
        COUVERT_PREMEDITE = 'CP'
        COUVERT_NON_PREMEDITE = 'CN'
        NON_PRECISE = 'NP'
    visage_couvert = models.CharField(max_length = 2, choices = Visage_couvert_enum.choices, default = Visage_couvert_enum.NON_PRECISE)

    class Etat_enum(models.TextChoices):
        IVRE = 'I'
        DROGUE = 'D'
        IVRE_ET_DROGUE = 'ID' #both
        NON_PRECISE = 'NP'
    etat_braqueur = models.CharField(max_length = 2, choices = Etat_enum.choices, default = Etat_enum.NON_PRECISE)

    class Attitude_enum(models.TextChoices):
        CALME = 'C'
        VIOLENT = 'V'
        NON_PRECISE = 'NP'
    attitude_braqueur = models.CharField(max_length = 2, choices = Attitude_enum.choices, default = Attitude_enum.NON_PRECISE)

    class Sexe_enum(models.TextChoices):
        MASC = 'M'
        FEM = 'F'
        NON_PRECISE = 'NP'
    sexe = models.CharField(max_length = 2, choices = Sexe_enum.choices, default = Sexe_enum.NON_PRECISE)
    connu_police = models.BooleanField(default = False)

    def __str__(self):
        return 'Braqueur '+str(self.id_braqueur)+'\t:'+'\tSexe '+self.sexe+'\tAge '+str(self.age)+'\tVisage '+self.visage_couvert+'\tEtat '+self.etat_braqueur+'\tAttitude '+self.attitude_braqueur+'\tConnu_police '+str(self.connu_police)

class Arme(models.Model):
    id_arme = models.AutoField(primary_key = True)
    nom_arme = models.CharField(max_length = 50)
    
    class Statut_arme_enum(models.TextChoices):
        ARME_BLANCHE = 'B'
        ARME_DE_POING = 'P'
        ARME_LONGUE = 'L'
        ARME_PAR_DESTINATION = 'D'
        ARME_INCAPACITANTE = 'I'
        NON_PRECISE = 'NP'
    statut_arme = models.CharField(max_length = 2, choices = Statut_arme_enum.choices, default = Statut_arme_enum.NON_PRECISE)

    def __str__(self):
        return self.nom_arme

class Article(models.Model):
    id_article = models.AutoField(primary_key = True)
    date_article = models.DateField()
    titre = models.CharField(max_length = 200)
    fk_source = models.ForeignKey(Source, on_delete = models.SET_NULL, blank = True, null = True, to_field='id_source')
    contenu = models.TextField(blank = True, null = True)

    def __str__(self):
        return 'Article ' + str(self.id_article) + '\t:\t' + self.titre +' - ' + self.fk_source.__str__() + ' - ' + str(self.date_article)

# one-to-many relationship with braquage
class Lieu(models.Model):
    id_lieu = models.AutoField(primary_key=True)
    nom_lieu = models.CharField(max_length = 50)
    fk_secu = models.ForeignKey(Securite, to_field = 'id_secu', on_delete = models.SET_NULL, blank = True, null = True)
    fk_ville = models.ForeignKey(Ville, on_delete = models.SET_NULL, blank = True, null = True)

    class Type_lieu_enum(models.TextChoices):
        PHARMACIE = 'PH'
        BUREAU_TABAC = 'BT'
        BANQUE = 'BQ'
        RESTAURANT = 'RT'
        BIJOUTERIE = 'BJ'
        SUPERMARCHE = 'SM'
        SUPERETTE = 'SU'
        AUTRE_COMMERCE = 'AC'
        AUTRE = 'AU'
        USINE = 'US'
        NON_PRECISE = 'NP'
    type_lieu = models.CharField(max_length = 2, choices = Type_lieu_enum.choices, default = Type_lieu_enum.NON_PRECISE)

    class Milieu_enum(models.TextChoices):
        URBAIN = 'UR'
        SUBURBAIN = 'SU'
        RURAL = 'RR'
        CENTRE_COMMERCIAL = 'CC'
        NON_PRECISE = 'NP'
    milieu = models.CharField(max_length = 2, choices = Milieu_enum.choices, default = Milieu_enum.NON_PRECISE)

    def __str__(self):
        return (self.nom_lieu +' (' + self.fk_ville.__str__() + ')')

# main table = Braquage
class Braquage(models.Model):
    id_braquage = models.AutoField(primary_key = True)
    date_braquage = models.DateField()
    nb_presents = models.IntegerField(blank = True, null = True)
    degats_mat = models.BooleanField(default = False)

    class Moment_enum(models.TextChoices):
        TOT = 'TO'
        MATIN = 'AM'
        MIDI = 'MI'
        APRES_MIDI = 'PM'
        SOIR = 'SO'
        NUIT = 'NU'
        NON_PRECISE = 'NP'
    moment_braquage = models.CharField(max_length = 2, choices = Moment_enum.choices, default = Moment_enum.NON_PRECISE)
    # one-to-many relationships
    fk_blesse = models.ForeignKey(Blesse, to_field = 'id_blesse', on_delete = models.SET_NULL, blank = True, null = True)
    fk_lieu = models.ForeignKey(Lieu, to_field = 'id_lieu', on_delete = models.SET_NULL, blank = True, null = True)
    # many-to-many relationships
    braqueurs = models.ManyToManyField(Braqueur)
    articles = models.ManyToManyField(Article)
    armes = models.ManyToManyField(Arme, through = 'Utilisation_arme', through_fields=('fk_braquage', 'fk_arme')) 
    def __str__(self):
        return 'Braquage '+str(self.id_braquage)+'\t:\t'+self.fk_lieu.__str__()+'\t'+str(self.date_braquage)


# transition table for many-to-many relationship with Arme only (other are generated automatically)
class Utilisation_arme(models.Model):
    fk_braquage = models.ForeignKey(Braquage, to_field = 'id_braquage', on_delete = models.SET_NULL, blank = True, null = True)
    fk_arme = models.ForeignKey(Arme, to_field = 'id_arme', on_delete = models.SET_NULL, blank = True, null = True)
    
    class Utilisation_enum (models.TextChoices):
        UTILISEE = 'U'
        MENACE = 'M'
        FEU_SUR_CIBLE = 'F'
        NON_UTILISEE = 'NU'
        NON_PRECISE = 'NP'
    utilisation = models.CharField(max_length = 2, choices = Utilisation_enum.choices, default = Utilisation_enum.NON_PRECISE)

    def __str__(self):
        return (self.fk_braquage.__str__() + ' <--> ' + self.fk_arme.__str__())


# one-to-one relationships with braquages
class Fuite(models.Model):
    fk_braquage = models.OneToOneField(Braquage,to_field = 'id_braquage', on_delete = models.SET_NULL, blank = True, null = True)

    class Butin_enum(models.TextChoices):
        ARGENT = 'A'
        OBJETS = 'O'
        ARGENT_ET_OBJETS = 'AO'
        RIEN = 'R'
        NON_PRECISE = 'NP'
    type_butin = models.CharField(max_length = 2, choices = Butin_enum.choices, default = Butin_enum.NON_PRECISE)
    valeur = models.IntegerField(blank = True, null = True)
    class Fuite_enum(models.TextChoices):
        A_PIED = 'P'
        MOTO = 'M'
        VOITURE = 'VP'
        NON_PRECISE = 'NP'
    type_fuite = models.CharField(max_length = 2, choices = Fuite_enum.choices, default = Fuite_enum.NON_PRECISE)

    def __str__(self):
        return 'Fuite : ' + str(self.fk_braquage)

class Arrestation_calme(models.Model):
    fk_braquage = models.OneToOneField(Braquage,to_field = 'id_braquage', on_delete = models.SET_NULL, blank = True, null = True)

    class Circonstances_enum (models.TextChoices):
        SUR_PLACE = 'SP'
        PENDANT_FUITE = 'PF'
        NON_PRECISE = 'NP'
    circonstances = models.CharField(max_length = 2, choices = Circonstances_enum.choices, default = Circonstances_enum.NON_PRECISE)
    
    def __str__(self):
        return 'Arrestation calme : ' + str(self.fk_braquage)

class Arrestation_musclee(models.Model):
    fk_braquage = models.OneToOneField(Braquage,to_field = 'id_braquage', on_delete = models.SET_NULL, blank = True, null = True)

    class Circonstances_enum (models.TextChoices):
        SUR_PLACE = 'SP'
        PENDANT_FUITE = 'PF'
        NON_PRECISE = 'NP'
    circonstances = models.CharField(max_length = 2, choices = Circonstances_enum.choices, default = Circonstances_enum.NON_PRECISE)

    usage_arme = models.BooleanField()
    intervention_ext = models.BooleanField()
    
    def __str__(self):
        return 'Arrestation musclée : ' + str(self.fk_braquage)

