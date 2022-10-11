s='''munchbox meals munchbox is a geelong-based boutique meal prep and delivery service,
specialising in artisan vegan and vegetarian meals and munchies. with a passion for
providing delicious and nutritious food that is ethical, sustainable and affordable, all
munchbox meals are made from scratch using a balance of the freshest local and organic
vegetables and fruit, grains, seeds and nuts and homegrown herbs. we chat to eden callick –
the brains behind the business – about all things munchbox. hey! thanks for chatting to forte!
first up, can you explain how munchbox became to be? munchbox was a daydream turned
reality. i was in a really draining job i hated, and would spend the majority of my lunch-break
looking for vegan food. the struggle to find a tasty, good quality, vegan meal is real.
sometimes it was so real i’d just give up looking, and go hungry. one day i hungrily and
jokingly announced, ‘i’m going to open my own vegan food business’ and with that impulsive
announcement, i quit my job almost immediately, and promised myself i would put my whole
heart and soul in to becoming the best vegan chef i can be. with a whole lot of determination,
passion and support from those around me, munchbox was born and is now my baby! i
guess a little bit of selfishness for me to have passion and purpose in life, as well as the lack
of real quality vegan cuisine on the geelong food scene is really how munchbox came to be
– out of necessity. where did your passion for vegan/vegetarian food come from? i’ve always
had a love and passion for food, but it wasn’t until i slowly transitioned to vegan that my
passion turned into a true obsession! it opened a whole new door for experimentation in the
kitchen; i want to create cruelty free food that tastes and looks better, but most importantly is
better for you! nothing makes me happier then feeding people and changing their views on
vegan food. can you give our readers a run-down of how ‘munchbox’ works? munchbox is
an artisan meal prep and delivery service, providing chef made meals to you. our munchers
can order online any time before friday midnight, with meals being ready for pick-up or
delivery on sunday. ready for the week ahead! these hours will soon be changing to include
24/7 online ordering, with pick-up and delivery between 7am-7pm seven days a week. all
meals come ready to eat or heat; those that are best enjoyed heated include a lit flame! we
also specialise in events and corporate catering; so, if there’s a bunch that’s got the munch,
we’re here to feed your sweet souls! where have you gathered most of your recipes and
ideas from? i’m constantly gathering ideas and inspiration from anywhere and everywhere! i
have a collection of paper scraps with scribbled recipes, and sleep with a notebook next to
my bed just in case i dream up a new idea. i have mood-boards, and future menu lists. it’s a
mess really! i find so much inspiration and ideas from traditional non-vegan meals, and have
been fortunate enough to work alongside some amazing non-vegan chefs who have (taught)
and inspired me incredibly. my mumma and sister, who are huge vegan foodies, are always
coming up with insane recipes for me as well. but each recipe is ultimately my own, made
from scratch, tried and tested until it’s perfected. how do you determine what local and
organic ingredients make the cut? we are passionately committed to sustainability and
supporting our local community. our menus are always based around the freshest seasonal
produce, sourced from local organic farmers, as well as other artisan vegan businesses who
supply some of our ingredients. we also lovingly grow all our own herbs, and as munchbox
expands so will our veggie garden; to include some pretty crazy exotic fruit and vege! what
type of people does this service suit? munchbox is perfect for those who are time poor, but
hungry, and care what they put in to their body. looking for a delicious and nutritious meal,
that isn’t frozen or full of crap. we put all the freshness, flavour, love and care into each meal,
so you don’t have to! breaky, lunch, or tea, pick up or delivery, we’ve got you covered so you
don’t have to think about cooking a thing! munchbox isn’t exclusively for vegetarians or
vegans, but is perfect for those looking to try a tasty healthy alternative! do you do custom
orders? or is everything off the set menu? yes! all our meals are fully customisable to suit
diet and taste! don’t like tomato? just let us know! gluten intolerant? we got you! you can add
or remove any ingredients and extras in our meals when you order. however, if you’d like our
chefs to create something extra special just for you, we’re more than happy to! we can
customise personalised menus, meal plans and munchboxes just for you! where are you
hoping to take munchbox in future? munchbox has big plans for the future! you can expect
an ever-changing menu (to keep up with my ever-changing mind). we’ll be incorporating
menulog and uber eats as apart of our service, and expanding trading hours and service
locations in the very near future. there may also be plans for ‘munch mobile’ to attend
festivals, markets, and events.. but i can’t give too much away! we have sooo many
surprises for ya’ll, but i can’t spoil them all at once! check it out via insta @vegan.munchbox
or you can get your munch on at munchboxmeals.com.au'''

ingredients=['Ambrette Seed','Apple Cinnamon Granola','Arizona Seasoning','Americano Coffee','Baby Abalone','Cadbury Double Decker Chocolate Bar',
'Campari Tomato','Celery Soup','Chia Meal','Crunch Bars','Cardamom','Giardiniera','Hog Maw','Mccormick Montreal Steak Seasoning',
'Muesli','Mulberry',
'Munch Chocolate','Murukku Packet','Mango','Organic Maize','Organic Peruvian Groundcherry','Organic Tartar Cream','Orange Extract',
'Pickled Cauliflower','Pork Chump Chops','Pork Lungs','Pork Tripe','Peanut Butter','Smokies Sausage','Snickers Spread',
'Strawberry Gelatin','Salmon','Tomato','Tamarind','Vegan Carob Chips','Vegan Chicken Strips','Vegan Chorizo',
'Vegan Marshmallow','Vegan Puff Pastry Sheet','Vegan Semisweet Chocolate Chips','Vegan White Cake','Vegetable Stock',
'Vinegar']

dict_ing={} #contains the key value pair for ingredients
for i in ingredients:
    dict_ing[i.lower()]=0   #initialising all the values to 0

import string
from time import time
import jellyfish
import nltk
from nltk.stem.porter import PorterStemmer

stemmer=PorterStemmer()
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import wordnet
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

punct = set(string.punctuation) 
s = "".join([ch for ch in s if ch not in punct])    #cleaning the text of puncuations

import re
s=re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", s)
stop_words=set(stopwords.words("english"))
s = " ".join([word for word in s.split() if word not in stop_words])    #cleaning the text of other connector words/articles etc. or speacial characters

#s now contains clean data
for i in s:
    for j in dict_ing:
        x=j
        A=nltk.word_tokenize(x)     #tokenizing the word
        B=nltk.pos_tag(A)           #attributing the type of word (noun, adjective, verb, adverb, etc.)
        try:
            for iter in B:
                if (iter[1]=="NN"):         #checking if the attribute is Noun
                    w1=wordnet.synset(iter[0]+".n.01")
                    w2=wordnet.synset(i+".n.01")
                    count=w1.wup_similarity(w2)         #doing a similarity check
                    if count>0.4:
                        dict_ing[j]+=1
                elif (iter[1]=="JJ"):       #checking if the attribute is Adjective
                    w1=wordnet.synset(iter[0]+".a.01")
                    w2=wordnet.synset(i+".a.01")
                    count=w1.wup_similarity(w2)         #doing a similarity check
                    if count>0.4:                       
                        dict_ing[j]+=1                  #incrementing the rank
        except:
            continue
        

dict_ing=[(a,b) for a,b in dict_ing.items()] # a list now
dict_ing.sort(key=lambda x:x[1])


l=[]                        #final printing of the ranked list
for i in dict_ing:
    if i[1]==0:
        l.append(i[0])
for i in l[::-1]:
    print(i)

for i in dict_ing:
    if i[1]!=0:
        print(i[0])
