import scala.io
import scala.collection.immutable.HashMap

object day02 {
    def main(args: Array[String]) = {
        val input = scala.io.Source.fromFile("../../inputs/day02.txt").mkString
        val rounds = input.split("\n").toArray
        var points = 0
        println(input)
        for (round <- rounds){
            points += choice_points(round.charAt(2).toString())
            points += results_points(round)
        }
        println(points)
    }

    def choice_points(choice: String): Int = {
        choice match {case "X" => 1 case "Y" => 2 case "Z" => 3}
    }

    def results_points(round: String): Int = {
        val player_choice = round.charAt(2).toString()
        val opponent_choice = round.charAt(0).toString()
        
        winLoseDraw(player_choice, opponent_choice)
    }

    def winLoseDraw(player: String, opponent: String) = {
        // A, B, C
        // X, Y, Z
        // R, P, S
        (opponent, player) match {
            case ("A", "X") => 3
            case ("A", "Y") => 0
            case ("A", "Z") => 6
            case ("B", "X") => 6
            case ("B", "Y") => 3
            case ("B", "Z") => 0
            case ("C", "X") => 0
            case ("C", "Y") => 6
            case ("C", "Z") => 3
        }
    }
}