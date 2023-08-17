import scala.io

object day04 {
    def main(args: Array[String]) = {
        val input = scala.io.Source.fromFile("../../inputs/day04.txt").mkString
        val sets = input.split("\n").toArray
        var count = 0
        for (set <- sets) {
          val pair = set.split(",").toArray
          val set1 = pair(0)
          val set2 = pair(1)
          if (contains(set1, set2) || contains(set2, set1)){
            count += 1
          }
        }
        println(count)
    }

    def contains(set: String, other: String) = {
      set.charAt(0).toInt <= other.charAt(0).toInt && set.charAt(2).toInt >= other.charAt(2).toInt
    }
}