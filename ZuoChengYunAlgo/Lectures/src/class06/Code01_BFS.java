package class06;

import java.util.HashSet;//insert, delete, modify, search --> O(1)
import java.util.LinkedList;
import java.util.Queue;

public class Code01_BFS {
    public static void bfs(Node node){
        if(node == null){
            return;
        }
        S
        Queue<Node> queue = new LinkedList<>();
        //in order to avoid the ring, so we prevent the node already checked by set.
        //检查去重的机制
        HashSet<Node> set = new HashSet<>();
        queue.add(node);
        set.add(node);
        while(!queue.isEmpty()){
            Node cur = queue.poll();
            System.out.println(cur.value);
            for(Node next : cur.nexts){
                if(!set.contains(next)){
                    set.add(next);
                    queue.add(next);
                }
            }
        }
    }
}
