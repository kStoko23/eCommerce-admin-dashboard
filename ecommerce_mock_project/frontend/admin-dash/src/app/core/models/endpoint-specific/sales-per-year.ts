/*
 * Model for monthly summary of sales and profits
 */

export interface SalesPerYear {
  month: Date;
  total_sales: number;
  total_profits: number;
}
