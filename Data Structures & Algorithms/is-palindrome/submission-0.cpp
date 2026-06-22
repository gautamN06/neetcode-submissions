class Solution {
public:
    bool isPalindrome(string s) {


        string clean = "";
        string reversed = "";

        //this cleans up the string and adds to clean string
        for(int i = 0; i < s.length(); i++)
        {
            if(isalnum(s[i]))
            {
                clean += tolower(s[i]);
            }

        }

        //next we should reverse the clean string 

        for(int j = clean.length()-1; j >= 0; j--)
        {
            reversed += clean[j];
        }

        //check if reversed and cleaned are same string

        
        if(reversed == clean)
            return true;
        else
            return false;
            

    }
};
