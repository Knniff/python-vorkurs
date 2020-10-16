class GameOfLife {
  constructor(width) {
    this.width = width;
    var grid = new Array(width);
    for (let index = 0; index < width; index++) {
      grid[index] = Array(this.width)
        .fill()
        .map(() => (Math.round(Math.random()) ? "😀" : "💀"));
    }
    this.grid = grid;
    this.print();
  }

  print() {
    const regex = /,/g;
    this.grid.forEach((row) => {
      console.log(row.toString().replace(regex, ""));
    });
    console.log();
  }

  is_alive(x, y) {
    if (x < 0 || y < 0 || x >= this.width || y >= this.width) {
      return 0;
    }
    if (this.grid[x][y] === "😀") {
      return 1;
    }
    return 0;
  }

  neighbor_count(x, y) {
    var living_neighbors = 0;

    for (let row_offset = -1; row_offset < 2; row_offset++) {
      if (row_offset === 0) {
        for (
          let column_offset = -1;
          column_offset < 2;
          column_offset = column_offset + 2
        ) {
          //console.log(x + row_offset, y + column_offset);
          living_neighbors += this.is_alive(x + row_offset, y + column_offset);
        }
      } else {
        for (let column_offset = -1; column_offset < 2; column_offset++) {
          //console.log(x + row_offset, y + column_offset);
          living_neighbors += this.is_alive(x + row_offset, y + column_offset);
        }
      }
    }
    return living_neighbors;
  }

  logic() {
    var newgrid = new Array(this.width);
    for (let index = 0; index < this.width; index++) {
      newgrid[index] = Array(this.width).fill("💀");
    }
    for (let x = 0; x < this.width; x++) {
      for (let y = 0; y < this.width; y++) {
        const living_neighbors = this.neighbor_count(x, y);
        if (this.is_alive(x, y) === 1) {
          if (living_neighbors === 3 || living_neighbors === 2) {
            newgrid[x][y] = "😀";
          }
        } else {
          if (living_neighbors === 3) {
            newgrid[x][y] = "😀";
          }
        }
      }
    }
    this.grid = newgrid;
    this.print();
  }
}

let game = new GameOfLife(5);

game.logic();
game.logic();
