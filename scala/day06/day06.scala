import scala.io

object day06 {
    def main(args: Array[String]) = {
        val input = scala.io.Source.fromFile("../../inputs/day06.txt").mkString
        val buffers = input.split("\n").toArray
        for (buffer <- buffers){
          var i = 0
          var notFound = true
          while (notFound && i <= (buffer.length() - 4)){
            if (buffer.substring(i, i + 4).distinct.length() == 4){
              println(i + 4)
              notFound = false
            }
            i += 1
          }
        }
    }
}