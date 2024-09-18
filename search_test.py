"""
Code to test BFS and DFS graph search.

To use it test method, you may need to install the gradescope decorators:
  pip install gradescope-utils
 
Author: Kevin Molloy
Version: 12/2022
"""

import unittest 
import search
import eightpuzzle
import driving
import sys
import queue 

from gradescope_utils.autograder_utils.decorators import weight, number

class SearchTests(unittest.TestCase):


    def run_test_bfs(self, test_to_run):
        """Helper function to test bfs
        
        Args:
            test_to_run (int): which of the puzzles to solve (loaded
            from loadEightPuzzle).

        Returns: nothing
        """

        """
        expected is a list of tuples that contains:
           -- the list of expected actions
           -- the cost of the set of actions (for the eightPuzzle, it 
                is equal to the length of the list since all actions
                have cost 1)
           -- the expected number of get operations from the frontier
           -- the expected number of put operations to the frontier
        """

        expected = [
            (['left'], 1, 3, 7),
            (['left', 'up', 'up', 'right', 'down', 'left', 'left', 'down',
             'right', 'right', 'up', 'left', 'up', 'right', 'down', 'left',
             'left', 'down', 'right', 'right', 'up', 'left', 'up', 'left'],
             23, 1 ,1),
            (['left', 'down', 'right', 'up', 'up', 'left', 'down', 
              'right', 'up', 'left'], 10, 813, 1292),
            (['up', 'left', 'down', 'right', 'up', 'right', 'down', 
             'left', 'up', 'left', 'down', 'right', 'up', 'left'], 14, 1 ,1)
        ]
        puzzle = eightpuzzle.loadEightPuzzle(test_to_run)
        problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)

        #print(problem.getStartState())
        
        path, cost, frontier_gets, frontier_puts = search.breadthFirstSearchStats(problem)
        self.assertEqual(expected[test_to_run][0], path,
            "\nAction list error on test with board:\n" + puzzle.__str__())
        self.assertEqual(expected[test_to_run][1],cost,
            "\nCost error on test with board:\n" + puzzle.__str__())
        self.assertAlmostEqual(expected[test_to_run][2], frontier_gets, delta=1,
            msg="\Explore count error on test with board:\n" + puzzle.__str__())
        self.assertAlmostEqual(expected[test_to_run][3], frontier_puts, delta=1,
            msg="\nFrontier put count error on test with board:\n" + puzzle.__str__())
    
    
    
    
    
    def verify_map_test(self, expected, student_results, msg):
        """Helper function to test driver/map based problems.
        
        This helper message allows all of the issues to be listed to
        the student, instead of just citing one problem and stopping
        the test (which is what assertEquals would do).

        Args:
            expected: a 4-tuple with the expected results
            student_results: a 4-tuple with the student results

            msg: a string to start with for appending information msgs.

        Returns: a 2-tuple
            True/False -- True indicates it passes, False otherwise
            msg: the modified String with informational messages
        """

        
        """
        Check that the student's code is returns a 4-tuple.
        """
    
        self.assertEqual(4,len(student_results),
            "Return should be a tuple of 4 values")

        test_ok = True  # assume the best

        ## break down 4-tuple into individual variables

        expected_path, expected_cost, expected_explored, expected_puts = expected
        student_path, student_cost, student_explored, student_puts = student_results

        if expected_path != student_path:
            test_ok = False
            msg += "\nexpected actions/path:" + str(expected_path) + \
                "\nstudent actions/path: " + str(student_path) + "\n"
        
        if expected_cost != student_cost:
            test_ok = False
            msg += "Cost mismatch.  Expected cost:" + str(expected_cost) + \
                " student cost:" + str(student_cost) + "\n"

        if abs(expected_explored - student_explored) > 1:
            test_ok = False
            msg += "Cost mismatch.  Expected explored:" + str(expected_explored) + \
                " student explored:" + str(student_explored) + "\n"
        
        if abs(expected_puts - student_puts) > 1:
            test_ok = False
            msg += "puts to frontier count mismatch. Expects puts:" \
                + str(expected_puts) + \
                " student puts:" + str(student_puts) + "\n"
        
        return test_ok, msg

    @weight(10)
    @number("1.0")
    def test_01_bfs_1(self):
        """BFS test on EightPuzzle 0"""
        self.run_test_bfs(0)

    @weight(10)
    @number("1.1")
    def test_02_bfs_2(self):
        """BFS test on EightPuzzle 2"""
        self.run_test_bfs(2)

    @weight(10)
    @number("1.2")     

    def test_03_bfs_3_map_1(self):
        """BFS test driving from Arad to Bucharest"""
        problem = driving.MapPuzzleProblem("Arad","Bucharest")
        expected_cost = 450
        expected_explored = 10
        expected_puts = 13

        expected = (['Sibiu', 'Fagaras', 'Bucharest'], expected_cost,
            expected_explored, expected_puts)

        test_ok = True
        failure_msg = "BFS Path from Sibiu to Bucharest. "

        student_results = search.breadthFirstSearchStats(problem)

        test_ok, failure_msg = self.verify_map_test(expected, student_results, failure_msg)

        self.assertEqual(True, test_ok, failure_msg)

    @weight(10)
    @number("2.0")     
    def test_04_dfs_1(self):
        """DFS on Eightpuzzle 0"""
        expected = [
            (['right', 'down', 'left', 'left', 'down', 'right', 'right', 'up', 
            'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 
            'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'right', 'up', 'left', 'left', 'down', 'right', 'up', 'right', 
            'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 
            'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 
            'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 
            'left', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 'down', 'right', 
            'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 
            'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 
            'left', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'left', 'up', 
            'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
            'left', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 
            'right', 'down', 'left', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 
            'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 
            'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'up', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
            'left', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 
            'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
            'left', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 
            'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 
            'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 
            'down', 'right', 'up', 'right', 'down', 'left', 'left', 'up', 'right', 
            'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 
            'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 
            'right', 'down', 'left', 'left', 'up', 'up', 'right', 'right', 'down', 
            'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 
            'right', 'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 
            'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 
            'right', 'up', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 
            'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 
            'up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 
            'down', 'left', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 
            'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'right', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 
            'left', 'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 
            'up', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
            'left', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 
            'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
            'left', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 
            'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 'right', 
            'up', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 'left', 
            'down', 'right', 'right', 'up', 'left', 'left', 'down', 'right', 'up', 
            'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 
            'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 
            'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 'left', 
            'left', 'up', 'up'],433,441,778),
            ([],0,0,0),
            ([],0,0,0),
            ([],0,0,0)
        ]
        for i in [0]:
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            #print(problem.getStartState())
            path, cost, explored, frontier_puts = search.depthFirstSearchStats(problem)
            self.assertEqual(expected[i][0], path,
                "\action list error on test with board:\n" + puzzle.__str__())
            self.assertEqual(expected[i][1],cost,
                "\nCost error on test with board:\n" + puzzle.__str__())
            self.assertAlmostEqual(expected[i][2],explored, delta=1,
                msg="\Explore count error on test with board:\n" + puzzle.__str__())
            self.assertAlmostEqual(expected[i][3],frontier_puts, delta=1,
                msg="\nFrontier put count error on test with board:\n" + puzzle.__str__())
    
    
    @weight(10)
    @number("2.1")     
    def test_05_dfs_2_map_1(self):
        """DFS driving test from Arad to Bucharest"""
        problem = driving.MapPuzzleProblem("Arad","Bucharest")
        expected_cost = 1119
        expected_explored = 10
        expected_puts = 16

        expected = (['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 
            'Pitesti', 'Rimnicu', 'Sibiu', 'Fagaras', 'Bucharest'], expected_cost,
            expected_explored, expected_puts)

        test_ok = True
        failure_msg = "DFS Path from Sibiu to Bucharest. "

        student_results = search.depthFirstSearchStats(problem)

        test_ok, failure_msg = self.verify_map_test(expected, student_results, failure_msg)

        self.assertEqual(True, test_ok, failure_msg)

    @weight(10)
    @number("2.2")     
    def test_06_dfs_3_map_2(self):
        """DFS driving test from Urziceni to Mehadia"""

        problem = driving.MapPuzzleProblem("Urziceni","Mehadia")
        expected_cost = 913
        expected_explored = 14
        expected_puts = 19

        expected = (['Bucharest', 'Fagaras', 'Sibiu', 'Rimnicu', 
            'Pitesti', 'Craiova', 'Drobeta', 'Mehadia'], expected_cost,
            expected_explored, expected_puts)

        test_ok = True
        failure_msg = "DFS Path from Urziceni to Mehadia. "

        student_results = search.depthFirstSearchStats(problem)

        test_ok, failure_msg = self.verify_map_test(expected, student_results, failure_msg)

        self.assertEqual(True, test_ok, failure_msg)

if __name__ == '__main__':
    unittest.main()
    