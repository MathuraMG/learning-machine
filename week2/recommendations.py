#A sample dataset for a recommendation engine for coffee
from math import sqrt

class recommendation():
    people={
    'mathura':{'CCD':2,'Kaapi':5,'Joes':3,'Starbucks':1},
    'madhu':{'CCD':1,'Kaapi':2,'Joes':4},
    'shroom':{'CCD':3,'Joes':5,'Starbucks':4},
    'sam':{'Kaapi':1,'Joes':2},
    'mathur':{'Kaapi':1,'Joes':2,'Starbucks':5}
    }

    def test(self):
        print 'hello'

    def compare(self,person1,person2):
        sum = 0
        for item in self.people[person1]:
            if item in self.people[person2]:
                sum+=pow((self.people[person1][item]-self.people[person2][item]),2)
        return 1/sqrt(1+sum)

    def topMatches(self,person_interest):
        scores = []
        for person in self.people:
            if person!=person_interest:
                scores.append((self.compare(person_interest,person),person))
        scores.sort();
        scores.reverse();
        print scores

    def getReco(self,person_interest):
        totals = {}
        no_review = {}
        ranking = {}
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
            ranking[item] = totals[item]/no_review[item]
        print totals
        print no_review
        print ranking

# from recommendations import recommendation
# reco = recommendation()
