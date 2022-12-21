/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */

const getCoordinates = (arr, i) => {
    const height = arr.length;
    const width = arr[0].length;
    let y = Math.floor(i / width);
    if (y >= height) {
        y = y % height;
    }
    const x = i % width;
    return { x: x, y: y };
};

const shiftGrid = (grid, k) => {
    const changes = k % (grid.length * grid[0].length);

    let arr = [];
    for (let i = 0, len = grid.length; i < len; i++) {
        arr[i] = [...grid[i]];
    }
    for (let i = 0, len = grid.length; i < len; i++) {
        for (let j = 0, len = grid[i].length; j < len; j++) {
            const shift = getCoordinates(
                grid,
                i * grid[0].length + j + changes
            );
            arr[shift.y][shift.x] = grid[i][j];
        }
    }
    return arr;
};

let grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
console.log(shiftGrid(grid, 1));
