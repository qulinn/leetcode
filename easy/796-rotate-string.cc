class Solution
{
public:
    bool rotateString(string s, string goal)
    {
        int l1 = s.length();
        int i = 0;
        bool ans = false;
        char temp = ' ';
        if (s == goal)
        {
            return true;
        }

        for (i = 1; i < l1; i++)
        {
            temp = s[0];
            s = s.substr(1, l1) + temp;
            if (s == goal)
            {
                ans = true;
                break;
            }
        }
        return ans;
    }
};