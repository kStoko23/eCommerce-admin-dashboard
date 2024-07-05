/* Model for popular product data,
 * contains product's id, name, category it belongs to,
 * count of how many it was ordered and
 * total profit made by selling this product
 */

export interface PopularProduct {
  product_id: number;
  product_name: string;
  category_name: string;
  order_count: number;
  total_profit: number;
}
