import numpy as np


def calculate(list):
    if not len(list) == 9:
        raise ValueError ("List must contain nine numbers.")

    else:
        npArray = np.array([
            [list[0],list[1],list[2]],
            [list[3],list[4],list[5]],
            [list[6],list[7],list[8]]
        ])

        meanArray = [np.mean(npArray, 0), np.mean(npArray, 1), np.mean(npArray)]
        varianceArray = [np.var(npArray, 0), np.var(npArray, 1), np.var(npArray)]
        stdArray = [np.std(npArray, 0), np.std(npArray, 1), np.std(npArray)]
        maxArray = [np.max(npArray, 0), np.max(npArray, 1), np.max(npArray)]
        minArray = [np.min(npArray, 0), np.min(npArray, 1), np.min(npArray)]
        sumArray = [np.sum(npArray, 0), np.sum(npArray, 1), np.sum(npArray)]

        calculations = {
            'mean': [meanArray[0].tolist(), meanArray[1].tolist(), meanArray[2].item()],
            'variance': [varianceArray[0].tolist(), varianceArray[1].tolist(), varianceArray[2].item()],
            'standard deviation': [stdArray[0].tolist(), stdArray[1].tolist(), stdArray[2].item()],
            'max': [maxArray[0].tolist(), maxArray[1].tolist(), maxArray[2].item()],
            'min': [minArray[0].tolist(), minArray[1].tolist(), minArray[2].item()],
            'sum': [sumArray[0].tolist(), sumArray[1].tolist(), sumArray[2].item()]
        }



    return calculations