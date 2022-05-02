package class06;

public class GraphGenerator {
    // N*3 matrix,
    public static Graph createGraph(Integer[][] matrix) { // assume [ 2, 1, 3] means [from, to, weight];
        Graph graph = new Graph();
        for (int i = 0; i < matrix.length; i++){
            Integer from = matrix[i][0];
            Integer to = matrix[i][1];
            Integer weight = matrix[i][2];
            //if 'from' node never appear
            if (!graph.nodes.containsKey(from)){
                graph.nodes.put(from, new Node(from));
            }
            //if 'to' node never appear
            if (!graph.nodes.containsKey(to)) {
                graph.nodes.put(to, new Node(to));
            }

            Node fromNode = graph.nodes.get(from);
            Node toNode = graph.nodes.get(to);

            //build new edge, or modify properties
            Edge newEdge = new Edge(weight, fromNode, toNode);
            //from out and point to 'to', so only add nexts
            fromNode.nexts.add(toNode);

            fromNode.out++;
            toNode.in++;

            fromNode.edges.add(newEdge);

            graph.edges.add(newEdge);
        }
        return graph;
    }
}