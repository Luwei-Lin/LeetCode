package class06;

import java.util.*;

public class Code03_TopologySort {
    public static List<Node> sortedTopology(Graph graph){
        //key : node
        //value: leftover 'in'
        HashMap<Node, Integer> inMap = new HashMap<>();
        //if ins == 0, enter the queue
        Queue<Node> zeroInQueue = new LinkedList<>();
        for(Node node: graph.nodes.values()){
            inMap.put(node, node.in);
            if(node.in == 0){
                zeroInQueue.add(node);
            }
        }
        //topology sort
        List<Node> result = new ArrayList<>();
        while(!zeroInQueue.isEmpty()){
            Node cur = zeroInQueue.poll();
            result.add(cur);
            for(Node next : cur.nexts){
                inMap.put(next, inMap.get(next) - 1);
                if(inMap.get(next) == 0){
                    zeroInQueue.add(next);
                }
            }
        }
        return result;
    }
}
