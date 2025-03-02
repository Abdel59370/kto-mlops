from typing import List

def count_long_names(names: List[str]) -> int:
    """
    Compte le nombre de prénoms dont la longueur dépasse 7 caractères.
    """
    long_name_count = sum(1 for name in names if len(name) > 7)
    
    for name in names:
        length_info = "supérieur à 7" if len(name) > 7 else "inférieur ou égal à 7"
        print(f"{name} est un prénom avec un nombre de lettres {length_info}")
    
    return long_name_count

if __name__ == "__main__":
    names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    count = count_long_names(names_list)
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {count}")
