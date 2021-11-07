
import csv
from django.core.management.base import BaseCommand

#import the models you will populate
from polls.models import Ville
from polls.models import Article
from polls.models import Source

class Command(BaseCommand):
    #def add_arguments(self,parser):
       # parser.add_argument('csv_file',type=str)
    
    def handle(self, *args,**options):
        data_list = []
        file_path = '/Users/mariegouilliard/Desktop/Nukkai/Braquage/Django_web/bd-braquages-master/brako/polls/csv_final_two.csv'
        with open(file_path,'r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.append(row)
                print(row)

        for i in range(len(data_list)):
            #organise data extracted from csv
            nom_s = data_list[i][0]
            date = data_list[i][1]
            titre_article = data_list[i][2]
            article_contenu = data_list[i][3]
            villes_nom = data_list[i][4]
            c_p = data_list[i][5] # this has to be 5 chars
            print("type:")
            print(type(c_p))
            print('Here',data_list[i][6])
            no_habitants = int(data_list[i][6]) #this has to be an integer
            print(type(no_habitants))
            
            #remplir la ville
            ville_instance, created = Ville.objects.get_or_create(code_postal = c_p,nom_ville = villes_nom, nb_habitants=no_habitants) 
            source_instance, created = Source.objects.get_or_create(nom_source = nom_s)
            #article_foreignkey = source_instance.id_source
            article_instance, created = Article.objects.get_or_create(date_article = date,titre=titre_article, fk_source = source_instance,contenu = article_contenu)
            




        


