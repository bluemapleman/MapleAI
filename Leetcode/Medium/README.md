# Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

- My Answer
```
package medium1;

import java.util.ArrayDeque;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class AddTwoNumbers
{
     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            StringBuilder str=new StringBuilder("");
            ArrayDeque<Integer> stack1=new ArrayDeque<Integer>();
            ArrayDeque<Integer> stack2=new ArrayDeque<Integer>();
            
            while(l1!=null){
                stack1.offer(l1.val);
                l1=l1.next;
            }
            while(l2!=null){
                stack2.offer(l2.val);
                l2=l2.next;
            }
            
            boolean jinwei=false;
            while(!stack1.isEmpty() && !stack2.isEmpty()){
                int ele1=stack1.poll(),ele2=stack2.poll();
                int sum;
                if(jinwei==true){
                    sum=ele1+ele2+1;
                }else{
                    sum=ele1+ele2;
                }

                jinwei=false;
                if(sum>=10)
                    jinwei=true;
                str.append(""+sum%10);
            }
            
            while(!stack1.isEmpty()){
                int ele=stack1.poll();
                if(jinwei==true){
                    str.append((ele+1)%10);
                    if(ele+1>=10){
                        jinwei=true;
                    }
                    else{
                        jinwei=false;
                    }
                }else{
                    str.append(ele);
                }
            }
            while(!stack2.isEmpty()){
                int ele=stack2.poll();
                if(jinwei==true){
                    str.append((ele+1)%10);
                    if(ele+1>=10){
                        jinwei=true;
                    }
                    else{
                        jinwei=false;
                    }
                }else{
                    str.append(ele);
                }
            }
            
            if(jinwei==true)
                str.append("1");
            
            
            
            int []arr=new int[str.length()];
            ListNode []nodeArr=new ListNode[arr.length];
            
            for(int i=0;i<str.length();i++){
                arr[i]=Character.digit(str.charAt(i), 10);
                nodeArr[i]=new ListNode(arr[i]);
                
            }
            
            for(int i=0;i<nodeArr.length-1;i++)
                nodeArr[i].next=nodeArr[i+1];
            return nodeArr[0];
        }
}

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}
```

# Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

- My Answer
```
package medium1;

import java.util.ArrayList;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class LongestSubstringWithoutRepeatingCharacters
{
    public static void main(String[] args)
    {
        
    }
    
    public int lengthOfLongestSubstring(String s) {
           if(s.equals("")) return 0;
                ArrayList<ArrayList<Character>> bigList=new ArrayList<ArrayList<Character>>(); 
                for(int i=0;i<s.length();i++){
                    ArrayList<Character> list=new ArrayList<Character>();
                    for(int j=i;j<s.length();j++){
                        if(list.contains(s.charAt(j))){
                            break;
                        }else{
                            list.add(s.charAt(j));
                        }
                    }
                    bigList.add(list);
                }
                
                int maxLen=Integer.MIN_VALUE;
                for(int i=0,len=bigList.size();i<len;i++){
                    ArrayList<Character> list=bigList.get(i);
                    if(list.size()>maxLen){
                        maxLen=list.size();
                    }
                }
                
                return maxLen;
      }
}
```

#  Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
```
Input: "babad"

Output: "bab"
```
Note: "aba" is also a valid answer.
 

Example:
```
Input: "cbbd"

Output: "bb"
```

- My Answer
```
package medium1;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class LongestPalindromicSubstring
{
    // This solution from: https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
    public static String longestPalindrome(String s) {
         int max = 0, idx = 0;
            for (int i = 0; i < s.length(); i++) {
                int len1 = extend(s, i, i), len2 = extend(s, i, i + 1);
                if (max < Math.max(len1, len2)) {
                    idx = (len1 > len2) ? (i - len1 / 2) : (i - len2 / 2 + 1);
                    max = Math.max(len1, len2);
                }
            }
            return s.substring(idx, idx + max);
     }
        
    private static int extend(String s, int i, int j) {
        for (; i >= 0 && j < s.length(); i--, j++)
            if (s.charAt(i) != s.charAt(j))
                break;
        return j - i - 2 + 1; // 2 means current two unmatched char
    }
    
    //Exceed time limit
//  public static String longestPalindrome(String s) {
//      if(s.length()<=1)
//          return s;
//      String answer="";
//      int len=s.length();
//      int findedPalindromMaxLen=0;
//      for(int i=0;i<len-1;i++) {
//          if(len-i<=findedPalindromMaxLen)
//              break;
//          for(int j=0;j<len-i;j++) {
////                System.out.println("len-j-i:"+(len-j-i));
//              if(len-j-i<=findedPalindromMaxLen)
//                  break;
//              
//              if(s.charAt(i)==s.charAt(len-j-1) && len-j-i>findedPalindromMaxLen) {
//                  String temp=s.substring(i,len-j);
//                  if(judgePalindrome(temp)) {
//                      if(temp.length()>findedPalindromMaxLen) {
//                          answer=temp;
//                          findedPalindromMaxLen=answer.length();
//                          System.out.println("longest:"+findedPalindromMaxLen+"iteration--i:"+i+",j:"+j);
//                      }
//                  }
//              }
//          }
//      }
//        return answer;
//    }
//  
//  public static boolean judgePalindrome(String s) {
//      int half=s.length()/2;
//      int len=s.length();
//      for(int i=0;i<half;i++) {
//          if(!(s.charAt(i)==s.charAt(len-i-1)))
//              return false;
//      }
//      return true;
//  }
}
```


#  ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string text, int nRows);
```

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

- My Answer
```
package medium1;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
public class ZigZagConversion
{
    
    // This solution from: https://leetcode.com/problems/zigzag-conversion/discuss/3403
    public String convert(String s, int numRows) {
        //Create numRows StringBuffers, and keep collecting characters from original string to corresponding StringBuffer. Just take care of your index to keep them in bound.

        char[] c = s.toCharArray();
        int len = c.length;
        StringBuffer[] sb = new StringBuffer[numRows];
        for (int i = 0; i < sb.length; i++) sb[i] = new StringBuffer();
        
        int i = 0;
        while (i < len) {
            for (int idx = 0; idx < numRows && i < len; idx++) // vertically down
                sb[idx].append(c[i++]);
            for (int idx = numRows-2; idx >= 1 && i < len; idx--) // obliquely up
                sb[idx].append(c[i++]);
        }
        for (int idx = 1; idx < sb.length; idx++)
            sb[0].append(sb[idx]);
        return sb[0].toString();
    }
}
```

# String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):

The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

- My Answer
```
package medium1;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
public class StringtoIntegeratoi
{
    public static void main(String[] args)
    {
        System.out.println(Character.digit('b',10));
    }
    
    
    // This solution from: https://leetcode.com/problems/string-to-integer-atoi/discuss/4654/My-simple-solution
    public static int myAtoi(String str) {
        int index = 0, sign = 1, total = 0;
        //1. Empty string
        if(str.length() == 0) return 0;

        //2. Remove Spaces
        while(str.charAt(index) == ' ' && index < str.length())
            index++;

        //3. Handle signs
        if(str.charAt(index) == '+' || str.charAt(index) == '-'){
            sign = str.charAt(index) == '+' ? 1 : -1;
            index ++;
        }
        
        //4. Convert number and avoid overflow
        while(index < str.length()){
            int digit = str.charAt(index) - '0';
            if(digit < 0 || digit > 9) break;

            //check if total will be overflow after 10 times and add digit
            if(Integer.MAX_VALUE/10 < total || Integer.MAX_VALUE/10 == total && Integer.MAX_VALUE %10 < digit)
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;

            total = 10 * total + digit;
            index ++;
        }
        return total * sign;
    }
    
    // This solution is from Java's library code: Integer.parseInt(String s), but it still can't cover all cases appeared in leetcode 
//  public static int myAtoi(String str) {
//          int radix=10;
//
//          int result = 0;
//          boolean negative = false;
//          int i = 0, len = str.length();
//          int limit = -Integer.MAX_VALUE;
//          int multmin;
//          int digit;
//
//          if (len > 0) {
//              char firstChar = str.charAt(0);
//              if (firstChar < '0') { // Possible leading "+" or "-"
//                  if (firstChar == '-') {
//                      negative = true;
//                      limit = Integer.MIN_VALUE;
//                  }
//
//                  if (len == 1) // Cannot have lone "+" or "-"
//                      return 0;
//                  i++;
//              }
//              multmin = limit / radix;
//              while (i < len) {
//                  // Accumulating negatively avoids surprises near MAX_VALUE
//                  digit = Character.digit(str.charAt(i++),radix);
//                  // illegal non-digit character
//                  if (digit < 0) {
//                          return 0;
//                  }
//                  if (result < multmin) {
//                      return 0;
//                  }
//                  result *= radix;
//                  if (result < limit + digit) {
//                      return 0;
//                  }
//                  result -= digit;
//              }
//          }
//          
//          return negative ? result : -result;
//   }
}
```

# Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

- My Answer
```
package medium1;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月11日
 */
public class ContainerWithMostWater
{
    // This solution from: https://leetcode.com/problems/container-with-most-water/discuss/6091/Easy-Concise-Java-O(N)-Solution-with-Proof-and-Explanation
    //  AKA, the general idea to find some max is to go through all cases where max value can possibly occur and keep updating the max value. The efficiency of the scan depends on the size of cases you plan to scan.
    //  To increase efficiency, all we need to do is to find a smart way of scan to cut off the useless cases and meanwhile 100% guarantee the max value can be reached through the rest of cases.
    //
    //  In this problem, the smart scan way is to set two pointers initialized at both ends of the array. Every time move the smaller value pointer to inner array. Then after the two pointers meet, all possible max cases have been scanned and the max situation is 100% reached somewhere in the scan. Following is a brief prove of this.
    //
    //  Given a1,a2,a3…an as input array. Lets assume a10 and a20 are the max area situation. We need to prove that a10 can be reached by left pointer and during the time left pointer stays at a10, a20 can be reached by right pointer. That is to say, the core problem is to prove: when left pointer is at a10 and right pointer is at a21, the next move must be right pointer to a20.
    //
    //  Since we are always moving the pointer with the smaller value, i.e. if a10 > a21, we should move pointer at a21 to a20, as we hope. Why a10 >a21? Because if a21>a10, then area of a10 and a20 must be less than area of a10 and a21. Because the area of a10 and a21 is at least height[a10] * (21-10) while the area of a10 and a20 is at most height[a10] * (20-10). So there is a contradiction of assumption a10 and a20 has the max area. So, a10 must be greater than a21, then next move a21 has to be move to a20. The max cases must be reached.
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            maxArea = Math.max(maxArea, Math.min(height[left], height[right])
                    * (right - left));
            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return maxArea;
    }
    // Still exceed time limit
    // For each line, they should try to find line that is at least as high as it and farthest from it.
//  public int maxArea(int[] height) {
//      int maxWater=0;
//      for(int i=0;i<height.length;i++) {
//          for(int start=0;start<i;start++) {
//              if(height[start]>=height[i]) {
//                  int capacity=height[i]*(i-start);
//                  if(capacity>maxWater)
//                      maxWater=capacity;
//                  break;
//              }
//          }
//          for(int end=height.length-1;end>i;end--) {
//              if(height[end]>=height[i]) {
//                  int capacity=height[i]*(end-i);
//                  if(capacity>maxWater)
//                      maxWater=capacity;
//                  break;
//              }
//          }
//      }
//      return maxWater;
//  }
    
    // Method of Exhaustion surely exceeds time limit!
//  public int maxArea(int[] height) {
//      int maxWater=0;
//      for(int i=0;i<height.length-1;i++) {
//          for(int j=i+1;j<height.length;j++) {
//              int capacity=(j-i)*Math.min(height[i], height[j]);
//              if(capacity>maxWater)
//                  maxWater=capacity;
//          }
//      }
//        return maxWater;
//    }
}
```

# 



