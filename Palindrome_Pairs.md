```java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        // 将所有字符反转一遍储存进map
        // 遍历字符串数组，找出a. 本身的反转， b.比本身短的搭档
        // 牛逼一点的做法，把words变成Trie, 然后搜索
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < words.length; i++) {
            StringBuilder word = new StringBuilder(words[i]);
            map.put(word.reverse().toString(), i);
        }
        
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        int index = -1;
        int cut = -1;
        for (int i = 0; i < words.length; i++) {
            // 找一样长的
            index = map.getOrDefault(words[i], -1);
            if (index >= 0 && index != i) {
                // 只放一个，剩下1个给对方来放
                ans.add(Arrays.asList(i, index));
            }
            // 找比它短的
            // 本身在前
            char[] ss = words[i].toCharArray();
            cut = ss.length - 1;
            while (cut >= 0) {
                // 确保切除掉的部分是个回文， 然后找剩下部分的反转
                if (isPldrm(ss, cut, ss.length - 1)) {
                    index = map.getOrDefault(words[i].substring(0, cut), -1);
                    if (index >= 0) {
                        ans.add(Arrays.asList(i, index));
                    }   
                }
                cut--;
            }
            
            // 本身在后
            cut = 0;
            while (cut <= ss.length - 1) {
                // 确保切除掉的部分是个回文， 然后找剩下部分的反转
                if (isPldrm(ss, 0, cut)) {
                    index = map.getOrDefault(words[i].substring(cut + 1, ss.length), -1);
                    if (index >= 0) {
                        ans.add(Arrays.asList(index, i));
                    }  
                }
                cut++;
            }
        }
        return ans;
    }
    private boolean isPldrm(char[] ss, int i, int j) {
        while (i < j) {
            if (ss[i++] != ss[j--]) {
                return false;
            }
        }
        return true;
    }
    
}
```

Solution 2 : make trie tree

```java
class Solution {
    
    class TrieNode{
        
        TrieNode[] children;
        int isEnd;
        ArrayList<Integer> word_id;
        
        
        public TrieNode(){
            children=new TrieNode[26];
            isEnd=-1;
            word_id=new ArrayList();
            
            
        } 
        
    }
    TrieNode root;
    public boolean isPalindrome(String s,int left,int right){
        
        //int right=s.length()-1;
        
        while(left<right){
            
            if(s.charAt(left++)!=s.charAt(right--)){
                return false;
            }
            
        }
        
        return true;
    }
    
    public void insert(String s,int idx){    
        TrieNode pcr=root;
        for (int level=s.length()-1; level>=0 ; level--){
            char c=s.charAt(level);
            
            
            if(pcr.children[c-'a']==null){
                
                pcr.children[c-'a']=new TrieNode();
            }
            if(isPalindrome(s,0,level)){
                pcr.word_id.add(idx);
            }
            pcr=pcr.children[c-'a'];
        }
        pcr.word_id.add(idx);
        pcr.isEnd=idx;   
    }
    public void search(int i,String s,List<List<Integer>> ans){
            TrieNode pcr=root;
            for( int j=0;j<s.length();j++){
                char c=s.charAt(j);
                //System.out.println(pcr.word_id);
                if(pcr.isEnd>=0 && pcr.isEnd!=i && isPalindrome(s,j,s.length()-1)){
                        //System.out.println("a-"+" "+i);
                        ans.add(Arrays.asList(i,pcr.isEnd));
                }
                
                pcr=pcr.children[c-'a']; 
                if(pcr==null){
                    //System.out.println("x"+" "+i);
                    return;
                }
                //System.out.println("a"+" "+i);
            }
           
            for(int k:pcr.word_id){
                //System.out.println("b"+" "+i);
                if(k==i)continue;
                ans.add(Arrays.asList(i,k));
                
            }
            
    }
   
    public List<List<Integer>> palindromePairs(String[] words) {
        
        List<List<Integer>> ans=new ArrayList();
        root=new TrieNode();
        
        for(int i=0;i<words.length;i++){
            
           
            
            insert(words[i],i);
            
        }
       
        
        for(int i=0;i<words.length;i++){
            
           
            
            search(i,words[i],ans);
            
        }
        return ans;
        
    }
}
```

Trie solution

```java
class Solution {
    
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> res = new LinkedList<>();
        TrieNode root = new TrieNode();
        for (int i = 0; i < words.length; i++) {
            constructTrie(words[i], root, i);
        }
        for (int i = 0; i < words.length; i++) {
            searchTrie(words[i], root, i, res);
        }
        return res;
    }
    
    private void constructTrie(String word, TrieNode root, int index) {
        char[] arr = word.toCharArray();
        TrieNode node = root;
        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if (node.next[c - 'a'] == null) {
                node.next[c - 'a'] = new TrieNode();
            }
            if (isPalindrome(word.substring(i))) {
                node.list.add(index);
            }
            node = node.next[c - 'a'];
        }
        node.list.add(index);
        node.index = index;
    }
    
    private boolean isPalindrome(String word) {
        char[] arr = word.toCharArray();  
        for (int i = 0; i < arr.length / 2; i++) {
            if (arr[i] != arr[arr.length - i - 1]) {
                return false;
            }
        }
        return true;
    }
    
    private void searchTrie(String word, TrieNode root, int index, List<List<Integer>> res) {
        char[] arr = word.toCharArray();
        TrieNode node = root;
        for (int i = arr.length - 1; i >= 0; i--) {
            char c = arr[i];
            if (isPalindrome(word.substring(0, i + 1)) && node.index != -1) {
                res.add(new LinkedList<>(Arrays.asList(node.index, index)));
            }
            node = node.next[c - 'a'];
            if (node == null) {
                return;
            }
        }
        for (int i : node.list) {
            if (i == index) {
                continue;
            }
            res.add(new LinkedList<>(Arrays.asList(i, index)));
        }
    }
}

class TrieNode {
    TrieNode[] next;
    int index;
    List<Integer> list;
    
    public TrieNode() {
        next = new TrieNode[26];
        index = -1;
        list = new ArrayList<>();
    }
}
```



Solution 3 : Map Matching 

```java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> wmap = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < words.length; i++)
            wmap.put(words[i], i);
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals("")) {
                for (int j = 0; j < words.length; j++) {
                    String w = words[j];
                    if (isPal(w, 0, w.length()-1) && j != i) {
                        ans.add(List.of(i, j));
                        ans.add(List.of(j, i));
                    }
                }
                continue;
            }
            StringBuilder sb = new StringBuilder(words[i]);
            sb.reverse();
            String bw = sb.toString();
            if (wmap.containsKey(bw)) {
                int res = wmap.get(bw);
                if (res != i) ans.add(List.of(i, res));
            }
            for (int j = 1; j < bw.length(); j++) {
                if (isPal(bw, 0, j-1)) {
                    String s = bw.substring(j);
                    if (wmap.containsKey(s))
                        ans.add(List.of(i, wmap.get(s)));
                }
                if (isPal(bw, j, bw.length()-1)) {
                    String s = bw.substring(0,j);
                    if (wmap.containsKey(s))
                        ans.add(List.of(wmap.get(s), i));
                }
            }
        }
        return ans;
    }
    
    private boolean isPal(String word, int i, int j) {
        while (i < j)
            if (word.charAt(i++) != word.charAt(j--)) return false;
        return true;
    }
}
```

