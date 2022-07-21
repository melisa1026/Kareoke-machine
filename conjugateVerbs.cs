using System;

public class conjugateVerbs
        {
            public bool isException = false;
            public string present;
            public string past;
            public string future;
            public string passive;

            conjugateVerbs(string present, string past, string future, string passive)
            {
                this.present = present;
                this.past = past;
                this.future = future;
                this.passive = passive;
            }
        }
        //list of unconjugated verbs
        class allVerbs
        {
            conjugateVerbs to_be = new conjugateVerbs("am", "will be", "have been", "being");  //declare to be
            conjugateVerbs to_wish = new conjugateVerbs("wish", "wished", "will wish", "wishing");
            conjugateVerbs to_have = new conjugateVerbs("have", "had", "will have", "having");
            conjugateVerbs to_do = new conjugateVerbs("do", "did", "will do", "doing");
            conjugateVerbs to_say = new conjugateVerbs("say", "said", "will say", "saying");
            conjugateVerbs to_go = new conjugateVerbs("go", "went", "will go", "going");
            conjugateVerbs to_get = new conjugateVerbs("get", "got", "will get", "getting");
            conjugateVerbs to_make = new conjugateVerbs("make", "made", "will make", "making");
            conjugateVerbs to_think = new conjugateVerbs("think", "thought", "will think", "thinking");
            conjugateVerbs to_take = new conjugateVerbs("take", "took", "will take", "taking");
            conjugateVerbs to_see = new conjugateVerbs("see", "saw", "will see", "seeing");
            conjugateVerbs to_come = new conjugateVerbs("come", "came", "will come", "coming");
            conjugateVerbs to_want = new conjugateVerbs("want", "wanted", "will want", "wanting");
            conjugateVerbs to_look = new conjugateVerbs("look", "looked", "will look", "looking");
            conjugateVerbs to_use = new conjugateVerbs("use", "used", "will use", "using");
            conjugateVerbs to_find = new conjugateVerbs("find", "found", "will find", "finding");
            conjugateVerbs to_give = new conjugateVerbs("give", "gave", "will give", "giving");
            conjugateVerbs to_tell = new conjugateVerbs("wish", "wished", "will wish", "wishing");
            conjugateVerbs to_work = new conjugateVerbs("work", "worked", "will work", "working");
            conjugateVerbs to_call = new conjugateVerbs("call", "called", "will call", "calling");
            conjugateVerbs to_try = new conjugateVerbs("try", "tried", "will try", "trying");
            conjugateVerbs to_ask = new conjugateVerbs("ask", "asked", "will ask", "asking");
            conjugateVerbs to_need = new conjugateVerbs("need", "needed", "will need", "needing");
            conjugateVerbs to_feel = new conjugateVerbs("feel", "felt", "will feel", "feeling");
            conjugateVerbs to_become = new conjugateVerbs("become", "becoming", "will become", "becoming");
            conjugateVerbs to_swim = new conjugateVerbs("swim", "swam", "will swim", "swimming");
            conjugateVerbs to_drown = new conjugateVerbs("drown", "drowned", "will drown", "drowning");
            conjugateVerbs to_ask = new conjugateVerbs("ask", "asked", "will ask", "asking");
            conjugateVerbs to_love = new conjugateVerbs("love", "loved", "will love", "loving");
            conjugateVerbs to_dream = new conjugateVerbs("dream", "dreamed", "will dream", "dreaming");
            conjugateVerbs to_hope = new conjugateVerbs("hope", "hoped", "will hope", "hoping");
            conjugateVerbs to_drink = new conjugateVerbs("drink", "drank", "will drink", "drinking");
            conjugateVerbs to_regret = new conjugateVerbs("regret", "regretted", "will regret", "regretting");
            conjugateVerbs to_wonder = new conjugateVerbs("wonder", "wondered", "will wonder", "wondering");

        }

        Nouns

    // class gives information about nouns
    class NounInfo
        {
            public string rhyme;
            public string syllables;
            public string verbs;
            public string adverbs;
            public string adjectives;
            public string determinants;
            public string categories;

            NounInfo(string rhyme, string syllables, string verbs, string adverbs, string adjectives,
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


}
