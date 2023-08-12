import scala.io

object day01 {
    def main(args: Array[String]) = {
        val input = io.Source.fromFile("../../inputs/day01.txt").getLines().toSeq
        val counts = input.map(customToInt(_)) 
        var calorie_count: Int = 0
        var calorie_counts: Seq[Int] = Seq()
        for (meal <- counts) {
            if (meal > 0) {
                calorie_count += meal
            }
            else {
                calorie_counts = calorie_counts :+ calorie_count
                calorie_count = 0
            }
        }
        println(calorie_counts.max)
    }

    def customToInt(s: String): Int = {
        try {
            Integer.parseInt(s.trim)
        } catch {
            case e: Exception => 0
        }
    }
}