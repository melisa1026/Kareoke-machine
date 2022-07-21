using System;

// class sorts nouns into categories
class SortNouns
{
    public string names;
    public string objects;
    public string jobs;
    public string art;
    public string companies;
}
//placing nouns into the categories
class allNouns
{
    SortNouns names = new SortNouns("Emma", "Claire", "Sonya", Melisa", "Erica", "Alexandra", "Alice", "Olivia", "Isabella", "Julia", "Mariam",
"Sophia", "Erica", "Pauline", "Mercedes", "Evelyn", "Theebika", "Anahita", "Maya", "Elsa", "Timbo", "Katherine",
"Sara", "Jolene", "Michael Jackson", "Celine Dion", "Taylor Swift", "Jack Black");
    SortNouns objects = new SortNouns("flower", "gun", "pen", "homemade elevator");
    SortNouns jobs = new SortNouns("doctor", "student", "engineer", "teacher", "clown", "accountant", "artist", "bouncer", "singer", "actor", "mailman", "dancer",
"soldier", "writer", "horseman", "lawyer", "model");
    SortNouns art = new SortNouns("painting", "sculpture", "song", "music", "makeup");
    SortNouns companies = new SortNouns("Nike", "Adidas", "Vogue", "Gucci");
    SortNouns emotions = new SortNouns("love", "hate", "angst", "jealousy", "disgust", "fear", "sadness", "lust", "romance")
    SortNouns animals = new SortNouns("dog", "cat", "ghost", "shark", "lion", "animal", "snake", "panda", "frog", "tiger", "bear", "cheetah", "eagle", "fox", "hound", "angel",
"devil", "stallion")
}

