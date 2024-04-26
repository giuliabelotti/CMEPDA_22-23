
#include "Phonebook.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>

using namespace std;

int main(){

    Contact Contatto1("Mario Rossi", "3405566778", "mario.rossi@gmail.com");
    Contact Contatto2("Guido Lamoto", "3339988776", "guido.lamoto1@gmail.com");
    Contact Contatto3("Remo Barca", "3335588991", "remo.barca@gmail.com");
   
    
    Contatto1.print();
    cout << " -----" << endl;
    Contatto2.print();
    cout << " -----" << endl;
    Contatto3.print();
          
    vector<Contact> Elenco_Telefonico({Contatto1, Contatto2, Contatto3}); 
    PhoneBook Agenda(Elenco_Telefonico);
    Agenda.Sort();
    
    pair <Contact,bool> risultato;
    risultato = Agenda.FindName(Contatto1);
    Agenda.Prefix();
    Agenda.Write_File();
    Agenda.load(); 

}
