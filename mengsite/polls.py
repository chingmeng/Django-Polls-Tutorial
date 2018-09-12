#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript polls
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: polls.models.Question

    from polls.models import Question

    polls_question_1 = Question()
    polls_question_1.question_text = 'How are you?'
    polls_question_1.pub_date = dateutil.parser.parse("2018-06-11T07:57:12.927873+00:00")
    polls_question_1 = importer.save_or_locate(polls_question_1)

    polls_question_2 = Question()
    polls_question_2.question_text = 'How mad are you?'
    polls_question_2.pub_date = dateutil.parser.parse("2018-06-11T07:57:34.837612+00:00")
    polls_question_2 = importer.save_or_locate(polls_question_2)

    polls_question_3 = Question()
    polls_question_3.question_text = 'How wrong are you?'
    polls_question_3.pub_date = dateutil.parser.parse("2018-06-11T07:57:55.751242+00:00")
    polls_question_3 = importer.save_or_locate(polls_question_3)

    polls_question_4 = Question()
    polls_question_4.question_text = 'How happy are you??'
    polls_question_4.pub_date = dateutil.parser.parse("2018-06-11T08:33:45+00:00")
    polls_question_4 = importer.save_or_locate(polls_question_4)

    # Processing model: polls.models.Choice

    from polls.models import Choice

    polls_choice_1 = Choice()
    polls_choice_1.question = polls_question_1
    polls_choice_1.choice_text = 'You are the man!'
    polls_choice_1.votes = 1
    polls_choice_1 = importer.save_or_locate(polls_choice_1)

    polls_choice_2 = Choice()
    polls_choice_2.question = polls_question_1
    polls_choice_2.choice_text = 'You are the best!'
    polls_choice_2.votes = 2
    polls_choice_2 = importer.save_or_locate(polls_choice_2)

    polls_choice_3 = Choice()
    polls_choice_3.question = polls_question_2
    polls_choice_3.choice_text = 'You are the man!'
    polls_choice_3.votes = 4
    polls_choice_3 = importer.save_or_locate(polls_choice_3)

    polls_choice_4 = Choice()
    polls_choice_4.question = polls_question_3
    polls_choice_4.choice_text = 'You are the one!'
    polls_choice_4.votes = 7
    polls_choice_4 = importer.save_or_locate(polls_choice_4)

    polls_choice_5 = Choice()
    polls_choice_5.question = polls_question_2
    polls_choice_5.choice_text = 'You are mad!'
    polls_choice_5.votes = 4
    polls_choice_5 = importer.save_or_locate(polls_choice_5)

    polls_choice_6 = Choice()
    polls_choice_6.question = polls_question_4
    polls_choice_6.choice_text = 'Very Happy'
    polls_choice_6.votes = 2
    polls_choice_6 = importer.save_or_locate(polls_choice_6)

    polls_choice_7 = Choice()
    polls_choice_7.question = polls_question_4
    polls_choice_7.choice_text = 'Damn Happy'
    polls_choice_7.votes = 3
    polls_choice_7 = importer.save_or_locate(polls_choice_7)

    polls_choice_8 = Choice()
    polls_choice_8.question = polls_question_4
    polls_choice_8.choice_text = 'Super duper Happy'
    polls_choice_8.votes = 3
    polls_choice_8 = importer.save_or_locate(polls_choice_8)

    # Processing model: polls.models.mModel

    from polls.models import mModel

    polls_mmodel_1 = mModel()
    polls_mmodel_1.name = 'Ahobaka'
    polls_mmodel_1.gender = 'M'
    polls_mmodel_1.age = 12
    polls_mmodel_1.email = 'aho@baka.com'
    polls_mmodel_1.dob = dateutil.parser.parse("2018-06-11")
    polls_mmodel_1.job = 'Student'
    polls_mmodel_1 = importer.save_or_locate(polls_mmodel_1)

    polls_mmodel_2 = mModel()
    polls_mmodel_2.name = 'Ultraman'
    polls_mmodel_2.gender = 'F'
    polls_mmodel_2.age = 23
    polls_mmodel_2.email = 'ultra@beam.ltd'
    polls_mmodel_2.dob = dateutil.parser.parse("2018-06-11")
    polls_mmodel_2.job = 'Superhero'
    polls_mmodel_2 = importer.save_or_locate(polls_mmodel_2)

    polls_mmodel_3 = mModel()
    polls_mmodel_3.name = 'Supergirl'
    polls_mmodel_3.gender = 'F'
    polls_mmodel_3.age = 26
    polls_mmodel_3.email = 'supergirl@centralcity.ny'
    polls_mmodel_3.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_3.job = 'Superheroin'
    polls_mmodel_3 = importer.save_or_locate(polls_mmodel_3)

    polls_mmodel_4 = mModel()
    polls_mmodel_4.name = 'Batgirl'
    polls_mmodel_4.gender = 'F'
    polls_mmodel_4.age = 21
    polls_mmodel_4.email = 'batgirl@centralcity.us'
    polls_mmodel_4.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_4.job = 'Superheroin'
    polls_mmodel_4 = importer.save_or_locate(polls_mmodel_4)

    polls_mmodel_5 = mModel()
    polls_mmodel_5.name = 'benghenglian'
    polls_mmodel_5.gender = 'M'
    polls_mmodel_5.age = 33
    polls_mmodel_5.email = 'default@default.com'
    polls_mmodel_5.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_5.job = 'BengHengLIanKnight'
    polls_mmodel_5 = importer.save_or_locate(polls_mmodel_5)

    polls_mmodel_6 = mModel()
    polls_mmodel_6.name = 'benghenglian'
    polls_mmodel_6.gender = 'M'
    polls_mmodel_6.age = 33
    polls_mmodel_6.email = 'default@default.com'
    polls_mmodel_6.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_6.job = 'BengHengLIanKnight'
    polls_mmodel_6 = importer.save_or_locate(polls_mmodel_6)

    polls_mmodel_7 = mModel()
    polls_mmodel_7.name = 'Superman'
    polls_mmodel_7.gender = 'm'
    polls_mmodel_7.age = 23
    polls_mmodel_7.email = 'default@default.com'
    polls_mmodel_7.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_7.job = 'Knight'
    polls_mmodel_7 = importer.save_or_locate(polls_mmodel_7)

    polls_mmodel_8 = mModel()
    polls_mmodel_8.name = 'Superman'
    polls_mmodel_8.gender = 'm'
    polls_mmodel_8.age = 23
    polls_mmodel_8.email = 'default@default.com'
    polls_mmodel_8.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_8.job = 'Knight'
    polls_mmodel_8 = importer.save_or_locate(polls_mmodel_8)

    polls_mmodel_9 = mModel()
    polls_mmodel_9.name = 'Superman'
    polls_mmodel_9.gender = 'm'
    polls_mmodel_9.age = 23
    polls_mmodel_9.email = 'default@default.com'
    polls_mmodel_9.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_9.job = 'Knight'
    polls_mmodel_9 = importer.save_or_locate(polls_mmodel_9)

    polls_mmodel_10 = mModel()
    polls_mmodel_10.name = 'Superman'
    polls_mmodel_10.gender = 'm'
    polls_mmodel_10.age = 23
    polls_mmodel_10.email = 'default@default.com'
    polls_mmodel_10.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_10.job = 'Knight'
    polls_mmodel_10 = importer.save_or_locate(polls_mmodel_10)

    polls_mmodel_11 = mModel()
    polls_mmodel_11.name = 'Superman'
    polls_mmodel_11.gender = 'm'
    polls_mmodel_11.age = 23
    polls_mmodel_11.email = 'default@default.com'
    polls_mmodel_11.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_11.job = 'Knight'
    polls_mmodel_11 = importer.save_or_locate(polls_mmodel_11)

    polls_mmodel_12 = mModel()
    polls_mmodel_12.name = 'Superman'
    polls_mmodel_12.gender = 'm'
    polls_mmodel_12.age = 23
    polls_mmodel_12.email = 'default@default.com'
    polls_mmodel_12.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_12.job = 'Knight'
    polls_mmodel_12 = importer.save_or_locate(polls_mmodel_12)

    polls_mmodel_13 = mModel()
    polls_mmodel_13.name = 'Superman'
    polls_mmodel_13.gender = 'm'
    polls_mmodel_13.age = 23
    polls_mmodel_13.email = 'default@default.com'
    polls_mmodel_13.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_13.job = 'Knight'
    polls_mmodel_13 = importer.save_or_locate(polls_mmodel_13)

    polls_mmodel_14 = mModel()
    polls_mmodel_14.name = 'Superman'
    polls_mmodel_14.gender = 'm'
    polls_mmodel_14.age = 23
    polls_mmodel_14.email = 'default@default.com'
    polls_mmodel_14.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_14.job = 'Knight'
    polls_mmodel_14 = importer.save_or_locate(polls_mmodel_14)

    polls_mmodel_15 = mModel()
    polls_mmodel_15.name = 'Superman'
    polls_mmodel_15.gender = 'd'
    polls_mmodel_15.age = 2
    polls_mmodel_15.email = 'default@default.com'
    polls_mmodel_15.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_15.job = 'Knight'
    polls_mmodel_15 = importer.save_or_locate(polls_mmodel_15)

    polls_mmodel_16 = mModel()
    polls_mmodel_16.name = 'Superman'
    polls_mmodel_16.gender = 'd'
    polls_mmodel_16.age = 2
    polls_mmodel_16.email = 'default@default.com'
    polls_mmodel_16.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_16.job = 'Knight'
    polls_mmodel_16 = importer.save_or_locate(polls_mmodel_16)

    polls_mmodel_17 = mModel()
    polls_mmodel_17.name = 'Superman'
    polls_mmodel_17.gender = 'd'
    polls_mmodel_17.age = 2
    polls_mmodel_17.email = 'default@default.com'
    polls_mmodel_17.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_17.job = 'Knight'
    polls_mmodel_17 = importer.save_or_locate(polls_mmodel_17)

    polls_mmodel_18 = mModel()
    polls_mmodel_18.name = 'Superman'
    polls_mmodel_18.gender = 'd'
    polls_mmodel_18.age = 2
    polls_mmodel_18.email = 'default@default.com'
    polls_mmodel_18.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_18.job = 'Knight'
    polls_mmodel_18 = importer.save_or_locate(polls_mmodel_18)

    polls_mmodel_19 = mModel()
    polls_mmodel_19.name = 'Superman'
    polls_mmodel_19.gender = 'd'
    polls_mmodel_19.age = 2
    polls_mmodel_19.email = 'default@default.com'
    polls_mmodel_19.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_19.job = 'Knight'
    polls_mmodel_19 = importer.save_or_locate(polls_mmodel_19)

    polls_mmodel_20 = mModel()
    polls_mmodel_20.name = 'Superman'
    polls_mmodel_20.gender = 'd'
    polls_mmodel_20.age = 2
    polls_mmodel_20.email = 'default@default.com'
    polls_mmodel_20.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_20.job = 'Knight'
    polls_mmodel_20 = importer.save_or_locate(polls_mmodel_20)

    polls_mmodel_21 = mModel()
    polls_mmodel_21.name = 'Superman'
    polls_mmodel_21.gender = 'd'
    polls_mmodel_21.age = 2
    polls_mmodel_21.email = 'default@default.com'
    polls_mmodel_21.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_21.job = 'Knight'
    polls_mmodel_21 = importer.save_or_locate(polls_mmodel_21)

    polls_mmodel_22 = mModel()
    polls_mmodel_22.name = 'Superman'
    polls_mmodel_22.gender = 'd'
    polls_mmodel_22.age = 2
    polls_mmodel_22.email = 'default@default.com'
    polls_mmodel_22.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_22.job = 'Knight'
    polls_mmodel_22 = importer.save_or_locate(polls_mmodel_22)

    polls_mmodel_23 = mModel()
    polls_mmodel_23.name = 'Superman'
    polls_mmodel_23.gender = 'c'
    polls_mmodel_23.age = 2
    polls_mmodel_23.email = 'default@default.com'
    polls_mmodel_23.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_23.job = 'Knight'
    polls_mmodel_23 = importer.save_or_locate(polls_mmodel_23)

    polls_mmodel_24 = mModel()
    polls_mmodel_24.name = 'Superman'
    polls_mmodel_24.gender = 'c'
    polls_mmodel_24.age = 2
    polls_mmodel_24.email = 'default@default.com'
    polls_mmodel_24.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_24.job = 'Knight'
    polls_mmodel_24 = importer.save_or_locate(polls_mmodel_24)

    polls_mmodel_25 = mModel()
    polls_mmodel_25.name = 'Superman'
    polls_mmodel_25.gender = 's'
    polls_mmodel_25.age = 2
    polls_mmodel_25.email = 'default@default.com'
    polls_mmodel_25.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_25.job = 'Knight'
    polls_mmodel_25 = importer.save_or_locate(polls_mmodel_25)

    polls_mmodel_26 = mModel()
    polls_mmodel_26.name = 'Superman'
    polls_mmodel_26.gender = 's'
    polls_mmodel_26.age = 2
    polls_mmodel_26.email = 'default@default.com'
    polls_mmodel_26.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_26.job = 'Knight'
    polls_mmodel_26 = importer.save_or_locate(polls_mmodel_26)

    polls_mmodel_27 = mModel()
    polls_mmodel_27.name = 'Superman'
    polls_mmodel_27.gender = 's'
    polls_mmodel_27.age = 2
    polls_mmodel_27.email = 'default@default.com'
    polls_mmodel_27.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_27.job = 'Knight'
    polls_mmodel_27 = importer.save_or_locate(polls_mmodel_27)

    polls_mmodel_28 = mModel()
    polls_mmodel_28.name = 'Superman'
    polls_mmodel_28.gender = 's'
    polls_mmodel_28.age = 2
    polls_mmodel_28.email = 'default@default.com'
    polls_mmodel_28.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_28.job = 'Knight'
    polls_mmodel_28 = importer.save_or_locate(polls_mmodel_28)

    polls_mmodel_29 = mModel()
    polls_mmodel_29.name = 'Superman'
    polls_mmodel_29.gender = 'g'
    polls_mmodel_29.age = 2
    polls_mmodel_29.email = 'default@default.com'
    polls_mmodel_29.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_29.job = 'Knight'
    polls_mmodel_29 = importer.save_or_locate(polls_mmodel_29)

    polls_mmodel_30 = mModel()
    polls_mmodel_30.name = 'Superman'
    polls_mmodel_30.gender = 'f'
    polls_mmodel_30.age = 2
    polls_mmodel_30.email = 'default@default.com'
    polls_mmodel_30.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_30.job = 'Knight'
    polls_mmodel_30 = importer.save_or_locate(polls_mmodel_30)

    polls_mmodel_31 = mModel()
    polls_mmodel_31.name = 'HOHOH'
    polls_mmodel_31.gender = 'M'
    polls_mmodel_31.age = 2
    polls_mmodel_31.email = 'default@default.com'
    polls_mmodel_31.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_31.job = 'DarkKinght'
    polls_mmodel_31 = importer.save_or_locate(polls_mmodel_31)

    polls_mmodel_32 = mModel()
    polls_mmodel_32.name = 'HOHOH'
    polls_mmodel_32.gender = 'M'
    polls_mmodel_32.age = 2
    polls_mmodel_32.email = 'default@default.com'
    polls_mmodel_32.dob = dateutil.parser.parse("2018-06-12")
    polls_mmodel_32.job = 'DarkKinght'
    polls_mmodel_32 = importer.save_or_locate(polls_mmodel_32)

    polls_mmodel_33 = mModel()
    polls_mmodel_33.name = 'PowerRangers'
    polls_mmodel_33.gender = 'M'
    polls_mmodel_33.age = 24
    polls_mmodel_33.email = 'powerranger@pw.pow'
    polls_mmodel_33.dob = dateutil.parser.parse("2018-05-12")
    polls_mmodel_33.job = 'Super Junior Heroes'
    polls_mmodel_33 = importer.save_or_locate(polls_mmodel_33)

    polls_mmodel_34 = mModel()
    polls_mmodel_34.name = 'Sherlock Holmes'
    polls_mmodel_34.gender = 'M'
    polls_mmodel_34.age = 44
    polls_mmodel_34.email = 'sherlock@england.uk'
    polls_mmodel_34.dob = dateutil.parser.parse("1901-03-14")
    polls_mmodel_34.job = 'Detective'
    polls_mmodel_34 = importer.save_or_locate(polls_mmodel_34)

    polls_mmodel_35 = mModel()
    polls_mmodel_35.name = 'Meng'
    polls_mmodel_35.gender = 'M'
    polls_mmodel_35.age = 31
    polls_mmodel_35.email = 'cm@cm.com'
    polls_mmodel_35.dob = dateutil.parser.parse("1987-04-01")
    polls_mmodel_35.job = 'Software Dev'
    polls_mmodel_35 = importer.save_or_locate(polls_mmodel_35)

    polls_mmodel_36 = mModel()
    polls_mmodel_36.name = 'ABCDE'
    polls_mmodel_36.gender = 'M'
    polls_mmodel_36.age = 25
    polls_mmodel_36.email = 'abcde@xya.css'
    polls_mmodel_36.dob = dateutil.parser.parse("2018-06-20")
    polls_mmodel_36.job = 'CSS Dev'
    polls_mmodel_36 = importer.save_or_locate(polls_mmodel_36)

    polls_mmodel_37 = mModel()
    polls_mmodel_37.name = 'Ali'
    polls_mmodel_37.gender = 'M'
    polls_mmodel_37.age = 24
    polls_mmodel_37.email = 'default@default.com'
    polls_mmodel_37.dob = dateutil.parser.parse("2018-06-20")
    polls_mmodel_37.job = 'Manager'
    polls_mmodel_37 = importer.save_or_locate(polls_mmodel_37)

