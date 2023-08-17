import scala.io

object day03 {
    def main(args: Array[String]) = {
        val input = scala.io.Source.fromFile("../../inputs/day03.txt").mkString
        val sacks = input.split("\n").toArray
        for (sack <- sacks){
          var half_1 = sack.substring(0, sack.length / 2)
          var half_2 = sack.substring(sack.length / 2 + 1, sack.length)
          println(findCommonElements(half_1, half_2))
        }
    }
    
    def findCommonElements(list1: String, list2: String) = {
      (list1 intersect list2).distinct
    }
}