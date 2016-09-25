#A sample dataset for a recommendation engine for coffee
from math import sqrt

class recommendation():

    people={
    'mathura':{'CCD':2,'Kaapi':5,'Joes':5,'Starbucks':1},
    'madhu':{'CCD':1,'Kaapi':5,'Joes':5},
    'shroom':{'CCD':3,'Kaapi':5,'Joes':5,'Starbucks':4},
    'sam':{'Kaapi':5,'Joes':5},
    'mathur':{'Kaapi':5,'Joes':5,'Starbucks':5}
    }

    movies={}

    movie_rating = {}

    def test(self):
        print 'hello'

    def getData(self):
        for line in open('movie_name.dat'):
            (id,title) = line.split('|')[0:2]
            self.movies[int(id.replace(" ",""))]=title.replace("\n","")
        for line in open('movie_rating.dat'):
            (user,movieid,rating) = line.split('|')[0:3]
            self.movie_rating.setdefault(int(user.replace(" ","")),{})
            self.movie_rating[int(user.replace(" ",""))][self.movies[int(movieid.replace(" ",""))]]=float(rating.replace(" ",""))

    def transform(self,data):
        result = {}
        for person in data:
            for item in data[person]:
                result.setdefault(item,{})
                result[item][person] = data[person][item]
        return result

    def compare(self,data,person1,person2):
        sum = 0
        for item in data[person1]:
            if item in data[person2]:
                sum+=pow((data[person1][item]-data[person2][item]),2)
        return 1/sqrt(1+sum)

    def topMatches(self,data,person_interest):
        scores = []
        for person in data:
            if person!=person_interest:
                scores.append((self.compare(data,person_interest,person),person))
        scores.sort()
        scores.reverse()
        return scores

    def getReco(self,data,person_interest):
        totals = {}
        no_review = {}
        ranking = []
        for person in data:
            if person!=person_interest:
                score = self.compare(data,person_interest,person)
                for item in data[person]:
                    if item not in data[person_interest]:
                        totals.setdefault(item,0)
                        no_review.setdefault(item,0)
                        totals[item]+=score*data[person][item]
                        no_review[item]+=score

        for item  in totals:
            ranking.append((totals[item]/no_review[item],item))
        ranking.sort()
        ranking.reverse()
        return ranking

    def getTop10Matches(self,data,person_interest):
        result = self.topMatches(data,person_interest)
        return result[0:10]

    def getTop10Reco(self,data,person_interest):
        result = self.getReco(data,person_interest)
        return result[0:10]

    def getTop10SimilarItem(self,data,item_interest):
        result = self.getSimilarItem(data,item_interest)
        return result[0:10]


    def getSimilarItem(self,data,item_interest):
        result = self.transform(data)
        output = self.topMatches(result,item_interest)
        return output

# from recommendations import recommendation
# reco = recommendation()
#
# reco.getData()
# reco.getTop10Reco(reco.movie_rating, 75)
# reco.getSimilarItem(reco.movie_rating, ' Synthetic Pleasures')
