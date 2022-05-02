package class06;

import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

public class Code05_Prim {
    public static class EdgeComparator implements Comparator<Edge> {

        @Override
        public int compare(Edge o1, Edge o2) {
            return o1.weight - o2.weight;
        }
    }

    public static Set<Edge> primMST(Graph graph){
        //min-heap edges
        PriorityQueue<Edge> priorityQueue = new PriorityQueue<>(new EdgeComparator());

        HashSet<Node> set = new HashSet<>();

        Set<Edge> result = new HashSet<>();// picked edges save in order in result

        for (Node node : graph.nodes.values()){ // randomly choose one node , this for loop is for forest problem in case

            if (!set.contains(node)) {
                set.add(node);
                for (Edge edge : node.edges){ //from one node, to unlock all relative edges
                    priorityQueue.add(edge);
                }
                while (!priorityQueue.isEmpty()){
                    Edge edge = priorityQueue.poll(); // poll the minimum-weight edge
                    Node toNode = edge.to; // this edge could have a new point
                    if ( !set.contains(toNode)) { // if node set doesn't, this node could be new node
                        set.add(toNode);
                        result.add(edge);
                        for (Edge nextEdge : toNode.edges){
                            priorityQueue.add(nextEdge);
                        }
                    }
                }
            }
            //break;
        }
        return result;
    }
}
