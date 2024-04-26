#ifndef PHONEBOOK_H
#define PHONEBOOK_H

using namespace std;

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <fstream>
#include <sstream>

class Contact {

    public: 
        Contact() {}
        Contact(const string& name, const string& phonenumber, const string& email) : m_name(name), m_phonenumber(phonenumber), m_email(email) {}
        
        string name() const {return m_name;}
        string phonenumber() const {return m_phonenumber;}
        string email() const {return m_email;}
        
        //setters
        void setphonenumber(string phonenumber) {m_phonenumber = phonenumber;} 
        
        void print() {
            cout << "Name: " << m_name << endl;
            cout << "Phone Number: " << m_phonenumber << endl; 
            cout << "Email: " << m_email << endl;
            
            map<string, string> othernumber;
            map<string, string>::iterator it = othernumber.begin();
            
            while (it !=othernumber.end()){
                cout << it->first << "->" << it->second << endl;
                it++;    
            }
        }
        
        bool operator<(const Contact & OtherName ){
            if(m_name < OtherName.m_name) return true;
            else return false;
        }
        
        bool operator==(const Contact & OtherName ){
            if(m_name == OtherName.m_name && m_phonenumber == OtherName.m_phonenumber && m_email == OtherName.m_email) return true;
            else return false;
        }
        
    private:
        string m_name;
        string m_phonenumber;
        string m_email;              
};

class PhoneBook {

    public:
    
        PhoneBook() {}        
        vector<Contact> m_Elenco;
        
        PhoneBook(vector<Contact> &Elenco) : m_Elenco(Elenco) {}
        
        void Sort() {
            sort(m_Elenco.begin(), m_Elenco.end());
        }
                
        pair <Contact,bool> FindName(Contact Person) {
        
            vector<Contact>::iterator it;
            it = find(m_Elenco.begin(), m_Elenco.end(), Person);
            
            if(it != m_Elenco.end()){
                cout << "Find!" << endl;
                pair <Contact, bool> product(Person, true);
                    return product;
            }
            else{
                cout << "Not find" << endl;
                pair <Contact, bool> product(Contact(), false);
                    return product;  
            }
        }
        

        static Contact ChangeNumber(Contact c1){
       
            string pref="+39";
            int found = c1.phonenumber().find(pref);
            
            if (found=string::npos){
                c1.setphonenumber(pref + c1.phonenumber());
                return c1;
            }
            
            else{ 
                return c1;
            }                
        }
       
        void Prefix(){
            transform (m_Elenco.begin(), m_Elenco.end(), m_Elenco.begin(), ChangeNumber); 
            cout << "Prefix added" << endl;   
        }
        
        void Write_File(){
            ofstream myfile;
            myfile.open("PhoneBook.txt");
            for(int i = 0; i < m_Elenco.size(); i++){
                myfile << m_Elenco[i].name() << " " << m_Elenco[i].phonenumber() << " " << m_Elenco[i].email() << endl;
            }
            myfile.close();
            cout << "PhoneBook created" << endl;
        }
        
        void load(){
            string line;
            ifstream myfile_in("PhoneBook.txt");
            if(myfile_in.is_open()){
                while(getline(myfile_in, line)){
                    cout << line << '\n';
                }
                myfile_in.close();
            }    
            else cout << "Unable to open file" << endl;
        }

};





#endif






