library(openxlsx)
library(httr)

# Tasa de intervención

link <- "https://totoro.banrep.gov.co/analytics/saw.dll?Download&Format=excel2007&Extension=.xlsx&BypassCache=true&path=%2Fshared%2fSeries%20Estad%c3%adsticas_T%2F1.%20Tasa%20de%20intervenci%C3%B3n%20de%20pol%C3%ADtica%20monetaria%2F1.2.TIP_Serie%20hist%C3%B3rica%20diaria%20IQY&lang=es&NQUser=publico&NQPassword=publico123&SyncOperation=1"

path_excel <- tempfile(fileext = ".xlsx")
r <- httr::GET(link)
bin <- httr::content(r, "raw")
writeBin(bin, path_excel)
x <- openxlsx::read.xlsx(path_excel, sheet = 1, detectDates = T)
deleted <- file.remove(path_excel)

x_wf <- x[-(1:5),]

db_TI <- x_wf[1:(nrow(x_wf) - 4),]
db_TI[,1] <- as.Date(db_TI[,1])
db_TI[,2] <- as.numeric(db_TI[,2])/100
colnames(db_TI) <- c("date", "interventionrate")
db_TI <- db_TI[order(db_TI$date),]
rownames(db_TI) <- NULL
View(db_TI)

class(db_TI[1,2])

# IBR

link <- "https://totoro.banrep.gov.co/analytics/saw.dll?Download&Format=excel2007&Extension=.xlsx&BypassCache=true&path=%2Fshared%2fSeries%20Estad%c3%adsticas_T%2F1.%20IBR%2F%201.1.IBR_Plazo%20overnight%20nominal%20para%20un%20rango%20de%20fechas%20dado%20IQY&lang=es&NQUser=publico&NQPassword=publico123&SyncOperation=1"

path_excel <- tempfile(fileext = ".xlsx")
r <- httr::GET(link)
bin <- httr::content(r, "raw")
writeBin(bin, path_excel)
x <- openxlsx::read.xlsx(path_excel, sheet = 1, detectDates = T)
View(x)
deleted <- file.remove(path_excel)


install.packages("macrocol")
library(macrocol)

# IPC

link <- "https://totoro.banrep.gov.co/analytics/saw.dll?Download&Format=excel2007&Extension=.xls&BypassCache=true&lang=es&NQUser=publico&NQPassword=publico123&path=%2Fshared%2FSeries%20Estad%C3%ADsticas_T%2F1.%20IPC%20base%202018%2F1.2.%20Por%20a%C3%B1o%2F1.2.5.IPC_Serie_variaciones"

path_excel <- tempfile(fileext = ".xlsx")
r <- httr::GET(link)
bin <- httr::content(r, "raw")
writeBin(bin, path_excel)
x <- openxlsx::read.xlsx(path_excel, sheet = 1, detectDates = T)
View(x)
deleted <- file.remove(path_excel)





