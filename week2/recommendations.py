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

    def test(self):
        print 'hello'

    def transform(self):
        result = {}
        for person in self.people:
            for item in self.people[person]:
                result.setdefault(item,{})
                result[item][person] = self.people[person][item]
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
        print scores

    def getReco(self,person_interest):
        totals = {}
        no_review = {}
        ranking = []
        for person in self.people:
            if person!=person_interest:
                score = self.compare(person_interest,person)
                for item in self.people[person]:
                    if item not in self.people[person_interest]:
                        totals.setdefault(item,0)
                        no_review.setdefault(item,0)
                        totals[item]+=score*self.people[person][item]
                        no_review[item]+=score

        for item  in totals:
            ranking.append((totals[item]/no_review[item],item))
        ranking.sort()
        ranking.reverse()
        print ranking

    def getSimilarItem(self,item_interest):
        result = self.transform()
        self.topMatches(result,item_interest)

# from recommendations import recommendation
# reco = recommendation()
