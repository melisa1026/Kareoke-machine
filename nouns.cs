using System;

// class gives information about nouns
class nouns
{
    public string rhyme;
    public string syllables;
    public string verbs;
    public string adverbs;
    public string adjectives;
    public string determinants;
    public string categories;

    nouns(string rhyme, string syllables, string verbs, string adverbs, string adjectives,
        string determinants, string categories)
    {
        this.rhyme = rhyme;
        this.syllables = syllables;
        this.verbs = verbs;
        this.adverbs = adverbs;
        this.adjectives = adjectives;
        this.determinants = determinants;
        this.categories = categories;
    }
}
//list of Nouns
class allNouns
{
    NounInfo flower = new NounInfo("ower", "2", "to_pick", "blissfully", "pretty", "the", "objects");  //information about flower and
    NounInfo Sonya = new NounInfo("ya", "2", "to_love", "really", "beautiful", "", "names");
}
